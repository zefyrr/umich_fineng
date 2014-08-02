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


		self.startIndex = None
		self.plotPrices = plotPrices
		self.plotDelta = plotDelta
		self.plotTheoreticalDelta = plotTheoreticals
		self.plotTheoreticalPrices = plotTheoreticals.twinx()
		self.plotAsset = plotAsset
		self.fig = fig
		self.line = self.drawPrices()
		self.drawDelta()

		fig.canvas.mpl_connect('pick_event', self.onPick)

		fig.autofmt_xdate(bottom=0.2, rotation=35, ha='right')
		plt.show()



	def drawPrices(self):
		plotPrices = self.plotPrices
		timestamps = self.timestamps
		stockPrices = self.stockPrices
		optionPrices = self.optionPrices

		plotStockPrices = plotPrices
		plotStockPrices.plot(timestamps, stockPrices, linestyle='-', marker='d', color='r', label='stock')
		plotStockPrices.set_ylabel('stock')
		plotStockPrices.legend(loc='upper left', fancybox=True)

		plotOptionPrices = plotPrices.twinx()
		line, = plotOptionPrices.plot(timestamps, optionPrices, linestyle='-', marker='o', color='b', label='option', picker=5)
		plotOptionPrices.set_ylabel('option')
		plotOptionPrices.legend(loc='upper right', fancybox=True)

		return line

	def drawDelta(self):
		plotDelta = self.plotDelta
		timestamps = self.timestamps
		spreadDeltas = self.spreadDeltas
		lastDeltas = self.lastDeltas


		plotDeltaSpread = plotDelta
		plotDeltaSpread.scatter(timestamps, spreadDeltas, marker='s', color='k', label='spread')
		plotDeltaSpread.set_ylabel('spread')
		plotDeltaSpread.legend(loc='upper left', fancybox=True)


		plotDeltaLast = plotDelta.twinx()
		plotDeltaLast.scatter(timestamps, lastDeltas, marker='x', color='g', label='last')
		plotDeltaLast.set_ylabel('last')
		plotDeltaLast.legend(loc='upper right', fancybox=True)

	def drawTheoreticals(self, tickIndex):
		theoreticalsForTick = self.theoreticals[tickIndex]
		prices = map(lambda x: x.price, theoreticalsForTick)
		deltas = map(lambda x: x.delta, theoreticalsForTick)
		ids = map(lambda x: x.Id.numDataPoints, theoreticalsForTick)

		plotTheoreticalDelta = self.plotTheoreticalDelta

		plotTheoreticalDelta.cla()
		plotTheoreticalDelta.set_title('Theoreticals')
		plotTheoreticalDelta.grid(True)
		plotTheoreticalDelta.plot(ids, deltas, color='k', label='delta')
		plotTheoreticalDelta.set_ylabel('delta')
		plotTheoreticalDelta.legend(loc='upper left', fancybox=True)

		plotTheoreticalPrices = self.plotTheoreticalPrices

		plotTheoreticalPrices.cla()
		plotTheoreticalPrices.grid(True)
		plotTheoreticalPrices.plot(ids, prices, color='b', label='price')
		plotTheoreticalPrices.set_ylabel('price')
		plotTheoreticalPrices.legend(loc='upper right', fancybox=True)


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

		prices = pandas.Series(prices)
		timestamps = self.timestamps[startIndex:endIndex]

		title = "Asset numDataPoints: %d delta :%f price: %f direction: %s" % (numDataPoints, delta, price, positionType)

		plotAsset = self.plotAsset

		plotAsset.cla()
		plotAsset.set_title(title)
		plotAsset.grid(True)
		plotAsset.plot(timestamps, prices, linestyle='-', marker='d', color='b', label='asset')
		plotAsset.set_ylabel('asset')
		plotAsset.legend(loc='upper right', fancybox=True)
		


	def onPick(self, event):
		if event.artist != self.line: 
			return True

		index = len(event.ind)

		if not index: 
			return True

		tickIndex = event.ind[0]

		self.drawTheoreticals(tickIndex)


		if not self.startIndex:
			self.startIndex = tickIndex
		else:
			if tickIndex > self.startIndex:
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

	args = parser.parse_args()

	if not args.datadir:
		parser.print_help()
		return

	if not os.path.exists(args.datadir):
		print 'Invalid path %s' % args.datadir
		return

	for root, dirnames, filenames in os.walk(args.datadir):
		for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
			pricedDataFile = root + "/" + filename
			print 'Processing file -', pricedDataFile 

			for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile, ('FDX1421F145')):
				empiricalData = processInstrument(optionMeta, pricedData)
				if empiricalData:
					plot = Plot(optionMeta, pricedData, empiricalData)

if __name__ == "__main__":
    main()






