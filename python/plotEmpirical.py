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


class TheoreticalBrowser:
	def __init__(self, theoreticals, plot):
		print 'instantiating', self
		self.theoreticals = theoreticals
		self.plot = plot

	def onPick(self, event):
		if event.artist!=line: return True
		print 'trying to print event', event
		index = len(event.ind)
		if not index: 
			return True

		print index

def processInstrument(optionMeta, pricedData):

	instrumentMeta = '%s %f %s' % (optionMeta.instrument, optionMeta.strike, getDateGMTFromUTCEpoch(optionMeta.expirationDate))

	print 'Processing -', instrumentMeta, 'ticks -', len(pricedData)
	firstPricedRecord = pricedData[0]

	if len(pricedData) <= 8:
		'Not enough ticks'
		return 

	return computeEmpiricals(pricedData, (0, len(pricedData) - 1))

def onpick(event):
	thisline = event.artist
	xdata = thisline.get_xdata()
	ydata = thisline.get_ydata()
	ind = event.ind
	print 'onpick points:', zip(xdata[ind], ydata[ind])

def plotInstrumentEmpiricals(instrumentMeta, processedDataList):

	fig, plots = plt.subplots(2, sharex=True)

	timestamps = []
	spreadDeltas = []
	lastDeltas = []
	optionPrices = []
	stockPrices = []

	for empiricalData in processedDataList:
		timestamps.extend(map(lambda x: x['timestamp'], empiricalData))
		timestamps.append(None)
		
		spreadDeltas.extend(map(lambda x: x['delta']['spread'], empiricalData))
		spreadDeltas.append(None)
		
		lastDeltas.extend(map(lambda x: x['delta']['last'], empiricalData))
		lastDeltas.append(None)

		optionPrices.extend(map(lambda x: x['optionTick'].last, empiricalData))
		optionPrices.append(None)
		
		stockPrices.extend(map(lambda x: x['underlyingTick'].last, empiricalData))
		stockPrices.append(None)

	stockPrices = pandas.Series(stockPrices)
	optionPrices = pandas.Series(optionPrices)
	lastDeltas = pandas.Series(lastDeltas)
	spreadDeltas = pandas.Series(spreadDeltas)
	timestamps = pandas.tseries.tools.to_datetime(timestamps, unit='ms')


	plotDelta = plots[0]
	plotDelta.set_title('Empirical Deltas')
	plotDelta.grid(True)

	plotPrices = plots[1]
	plotPrices.set_title('Prices')
	plotPrices.grid(True)


	plotDeltaSpread = plotDelta
	plotDeltaSpread.scatter(timestamps, spreadDeltas, marker='s', color='k', label='spread')
	plotDeltaSpread.set_ylabel('spread')
	plotDeltaSpread.legend(loc='upper left', fancybox=True)


	plotDeltaLast = plotDelta.twinx()
	plotDeltaLast.scatter(timestamps, lastDeltas, marker='x', color='g', label='last')
	plotDeltaLast.set_ylabel('last')
	plotDeltaLast.legend(loc='upper right', fancybox=True)


	plotStockPrices = plotPrices
	plotStockPrices.plot(timestamps, stockPrices, linestyle='-', marker='d', color='r', label='stock')
	plotStockPrices.set_ylabel('stock')
	plotStockPrices.legend(loc='upper right', fancybox=True)

	plotOptionPrices = plotPrices.twinx()
	line, = plotOptionPrices.plot(timestamps, optionPrices, linestyle='-', marker='o', color='b', label='option', picker=5)
	plotOptionPrices.set_ylabel('option')
	plotOptionPrices.legend(loc='upper left', fancybox=True)


	plotPrices.set_xlabel(instrumentMeta, fontsize=14)

	browser = TheoreticalBrowser(None, None)

	fig.canvas.mpl_connect('pick_event', onpick)

	fig.autofmt_xdate(bottom=0.2, rotation=35, ha='right')
	plt.show()




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

	processedDataMap = {}
	for root, dirnames, filenames in os.walk(args.datadir):
		for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
			pricedDataFile = root + "/" + filename
			print 'Processing file -', pricedDataFile 

			for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile, ('FDX1421F145')):
				instrumentMeta = getInstrumentMetaStr(optionMeta)
				processedData = processInstrument(optionMeta, pricedData)
				if processedData:
					processedDataList = processedDataMap.get(instrumentMeta, [])
					processedDataList.append(processedData)
					processedDataMap[instrumentMeta] = processedDataList

	for instrumentMeta in processedDataMap.keys():
		plotInstrumentEmpiricals(instrumentMeta , processedDataMap[instrumentMeta])

		if raw_input("Press 'q' and then enter to quit, or enter to continue\n").lower() == 'q':
			return


if __name__ == "__main__":
    main()






