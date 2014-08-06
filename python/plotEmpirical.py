import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import matplotlib.pyplot as plt
import math, pandas
import time
from readProto import getInstrumentIterator
from utils import getDateGMTFromUTCEpoch, getTimeInSecs, getInstrumentMetaStr
from empiricalDelta import computeEmpiricals
import itertools
import numpy as np
from drawDown import computeMinMax
import pprint
pp = pprint.PrettyPrinter(indent=2)

class Plot:
	def __init__(self, optionMeta, pricedData, empiricalData):
		self.optionMeta = optionMeta
		self.pricedData = pricedData
		self.empiricalData = empiricalData


		fig = plt.figure()
		instrumentMeta = getInstrumentMetaStr(optionMeta)
		fig.suptitle(instrumentMeta,  fontsize=18, fontweight='bold')

		plotPrices = fig.add_subplot(411)
		plotPrices.set_title('Prices')
		plotPrices.grid(True)

		plotDelta = fig.add_subplot(412, sharex=plotPrices)
		plotDelta.set_title('Empirical Deltas')
		plotDelta.grid(True)

		plotTheoreticals = fig.add_subplot(413)
		plotAsset = fig.add_subplot(414)
		

		self.stockPrices = pandas.Series(map(lambda x: x['underlyingTick'].last, empiricalData))
		self.optionPrices = pandas.Series(map(lambda x: x['optionTick'].last, empiricalData))
		self.lastDeltas = pandas.Series(map(lambda x: x['delta']['last'], empiricalData))
		self.spreadDeltas = pandas.Series(map(lambda x: x['delta']['spread'], empiricalData))
		self.timestamps = pandas.tseries.tools.to_datetime(map(lambda x: x['timestamp'], empiricalData), unit='ms')
		self.theoreticals = map(lambda x: x['theoreticals'], empiricalData)
		self.timestampStrs = map(lambda x: x['timestampStr'], empiricalData)


		self.startIndex = None
		self.startPositionAnnotation = None
		self.endPositionAnnotation = None

		self.plotStockPrices = plotPrices
		self.plotOptionPrices = plotPrices.twinx()
		self.plotDelta = plotDelta
		self.plotTheoreticalDelta = plotTheoreticals
		self.plotTheoreticalPrices = plotTheoreticals.twinx()
		self.plotAsset = plotAsset
		self.fig = fig
		self.line = self.drawPrices()
		self.drawDelta()

		fig.canvas.mpl_connect('pick_event', self.onPick)

		fig.autofmt_xdate(bottom=0.2, rotation=35, ha='right')
		fig.subplots_adjust(hspace=0.7)
		plt.show()


	def drawPrices(self):
		timestamps = self.timestamps
		stockPrices = self.stockPrices
		optionPrices = self.optionPrices

		plotStockPrices = self.plotStockPrices
		lnStock, = plotStockPrices.plot(timestamps, stockPrices, linestyle='-', marker='d', color='r', label='stock')
		plotStockPrices.set_ylabel('stock')

		plotOptionPrices = self.plotOptionPrices
		lnOption, = plotOptionPrices.plot(timestamps, optionPrices, linestyle='-', marker='o', color='b', label='option', picker=5)
		plotOptionPrices.set_ylabel('option')
		plotOptionPrices.set_xlim(timestamps[0], timestamps[-1])
		plotOptionPrices.set_ylim(plotOptionPrices[0] - 2, plotOptionPrices[-1] + 2)


		lns = [lnStock, lnOption]
		labs = [l.get_label() for l in lns]
		plotOptionPrices.legend(lns, labs, fancybox=True, bbox_to_anchor=(1.03, 1), loc=2, borderaxespad=0.0)

		return lnOption

	def drawDelta(self):
		plotDelta = self.plotDelta
		timestamps = self.timestamps
		spreadDeltas = self.spreadDeltas
		lastDeltas = self.lastDeltas


		plotDeltaSpread = plotDelta
		scatterSpread = plotDeltaSpread.scatter(timestamps, spreadDeltas, marker='s', color='k', label='spread')
		plotDeltaSpread.set_ylabel('spread')


		plotDeltaLast = plotDelta.twinx()
		scatterLast = plotDeltaLast.scatter(timestamps, lastDeltas, marker='x', color='g', label='last')
		plotDeltaLast.set_ylabel('last')

		lns = [scatterSpread, scatterLast]
		labs = [l.get_label() for l in lns]
		plotDeltaLast.legend(lns, labs, fancybox=True, bbox_to_anchor=(1.03, 1), loc=2, borderaxespad=0.0)

	def drawTheoreticals(self, tickIndex):
		theoreticalsForTick = self.theoreticals[tickIndex]
		prices = map(lambda x: x.price, theoreticalsForTick)
		deltas = map(lambda x: x.delta, theoreticalsForTick)
		ids = map(lambda x: x.Id.numDataPoints, theoreticalsForTick)

		plotTheoreticalDelta = self.plotTheoreticalDelta
		plotTheoreticalDelta.cla()
		plotTheoreticalDelta.set_title('Theoreticals @ ' + self.timestampStrs[tickIndex])
		plotTheoreticalDelta.grid(True)
		lnDelta, = plotTheoreticalDelta.plot(ids, deltas, color='k', label='delta')
		plotTheoreticalDelta.set_ylabel('delta')

		plotTheoreticalPrices = self.plotTheoreticalPrices
		plotTheoreticalPrices.cla()
		plotTheoreticalPrices.grid(True)
		lnPrice, = plotTheoreticalPrices.plot(ids, prices, color='b', label='price')
		plotTheoreticalPrices.set_ylabel('price')

		lns = [lnDelta, lnPrice]
		labs = [l.get_label() for l in lns]
		plotTheoreticalPrices.legend(lns, labs, fancybox=True, bbox_to_anchor=(1.03, 1), loc=2, borderaxespad=0.0)


	def drawAsset(self, startIndex, endIndex):
		minMax = computeMinMax(self.pricedData, (startIndex, endIndex))
		if not minMax:
			return

		theoretical = minMax['theoretical']
		direction = minMax['direction']

		positionType = "Buy" if direction == 1 else "Sell"
		numDataPoints = theoretical.Id.numDataPoints
		delta = theoretical.delta
		price = theoretical.price

		prices = []
		for i in range(startIndex, endIndex):		
			pricedRecord = self.pricedData[i]

			optionPrice = pricedRecord.pairedTick.optionTick.last
			underlyingPrice = pricedRecord.pairedTick.underlyingTick.last

			positionValue = direction * (optionPrice - (underlyingPrice * delta))
			prices.append(positionValue)

		profit = prices[-1] - prices[0]
		prices = pandas.Series(prices)
		timestamps = self.timestamps[startIndex:endIndex]

		title = "Asset\nid: %d delta :%f price: %f direction: %s" % (numDataPoints, delta, price, positionType)

		plotAsset = self.plotAsset

		plotAsset.cla()
		plotAsset.set_title(title)
		plotAsset.grid(True)
		lnModel, = plotAsset.plot(timestamps, prices, linestyle='-', marker='d', color='b', label='asset p/l : %0.2f' % profit)
		plotAsset.set_ylabel('price')
		plotAsset.legend(loc='upper right', fancybox=True)
		plotAsset.set_xlim(timestamps[0] - pandas.DateOffset(minutes=5), timestamps[-1] + pandas.DateOffset(minutes=5))

		lns = [lnModel]
		labs = [l.get_label() for l in lns]
		plotAsset.legend(lns, labs, fancybox=True, bbox_to_anchor=(1.03, 1), loc=2, borderaxespad=0.0)

	def drawAnnotation(self, x, y, tickIndex, plot, offets=(-30, 30)):
		text = "option: %0.2f\nstock: %0.2f\ntimestamp: %s"
		text = text % (self.optionPrices[tickIndex], self.stockPrices[tickIndex], self.timestampStrs[tickIndex])

		annotation = plot.annotate(text, xy=(x, y), ha='left',
		xytext=offets, textcoords='offset points', va='bottom',
		bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.85),
		arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0')
		)
		annotation.set_visible(True)
		return annotation

	def drawStartPositionAnnotation(self, x, y, tickIndex):
		self.startPositionAnnotation = self.drawAnnotation(x, y, tickIndex, self.plotOptionPrices)

	def drawEndPositionAnnotation(self, x, y, tickIndex):
		self.endPositionAnnotation = self.drawAnnotation(x, y, tickIndex, self.plotOptionPrices)

	def clearPositionAnnotation(self):
		try:
			if self.startPositionAnnotation:
				self.startPositionAnnotation.remove()
			if self.endPositionAnnotation:
				self.endPositionAnnotation.remove()
		except:
			pass


	def onPick(self, event):
		if event.artist != self.line: 
			return True

		index = len(event.ind)

		if not index: 
			return True

		tickIndex = event.ind[0]


		x, y = event.mouseevent.xdata, event.mouseevent.ydata

		if not self.startIndex:
			self.startIndex = tickIndex
			self.clearPositionAnnotation()
			self.drawStartPositionAnnotation(x, y, tickIndex)
			self.drawTheoreticals(tickIndex)
		else:
			if tickIndex > self.startIndex:
				self.drawEndPositionAnnotation(x, y, tickIndex)
				self.drawAsset(self.startIndex, tickIndex)
			self.startIndex = None

		self.fig.canvas.draw()



def processInstrument(optionMeta, pricedData):
	instrumentMeta = getInstrumentMetaStr(optionMeta)
	print 'Processing -', instrumentMeta, 'ticks -', len(pricedData)
	firstPricedRecord = pricedData[0]

	if len(pricedData) <= 8:
		'Not enough ticks'
		return 

	return computeEmpiricals(pricedData, (0, len(pricedData) - 1))


def main():
	parser = argparse.ArgumentParser(description="Run analysis")
	parser.add_argument('-d', '--datadir', help='location of priced data')
	parser.add_argument('-o', '--option', help='option to run analysis on')

	args = parser.parse_args()

	if not args.datadir:
		parser.print_help()
		return

	if not args.option:
		parser.print_help()
		return		

	if not os.path.exists(args.datadir):
		print 'Invalid path %s' % args.datadir
		return

	for root, dirnames, filenames in os.walk(args.datadir):
		for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
			pricedDataFile = root + "/" + filename
			print 'Processing file -', pricedDataFile 

			for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile, (args.option)):
				empiricalData = processInstrument(optionMeta, pricedData)
				if empiricalData:
					plot = Plot(optionMeta, pricedData, empiricalData)

if __name__ == "__main__":
    main()






