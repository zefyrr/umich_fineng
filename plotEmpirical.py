import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import matplotlib.pyplot as plt
import math, pandas
import time
from readProto import getInstrumentIterator
from utils import getTimeGMTFromUTCEpoch, getTimeInSecs, getInstrumentMetaStr
from empiricalDelta import computeEmpiricals
import itertools
import numpy as np
from profitAndLoss import computeNakedProfit


def processInstrument(optionMeta, pricedData):

	instrumentMeta = '%s %f %s' % (optionMeta.instrument, optionMeta.strike, getTimeGMTFromUTCEpoch(optionMeta.expirationDate))

	print 'Processing -', instrumentMeta, 'ticks -', len(pricedData)
	firstPricedRecord = pricedData[0]

	if len(pricedData) <= 8:
		'Not enough ticks'
		return 

	return computeEmpiricals(pricedData, (0, len(pricedData) - 1))


# class PointBrowser:
#     def __init__(self, ):



def plotInstrumentEmpiricals(instrumentMeta, processedDataList):

	fig, plots = plt.subplots(2, sharex=True)

	timestamps = []
	spreadDeltas = []
	lastDeltas = []
	optionPrices = []
	stockPrices = []

	for empiricalData in processedDataList:
		timestamps.extend(map(lambda x: x['timestamp'], empiricalData))
		timestamps.append(timestamps[-1])
		
		spreadDeltas.extend(map(lambda x: x['delta']['spread'], empiricalData))
		spreadDeltas.append(np.nan)
		
		lastDeltas.extend(map(lambda x: x['delta']['last'], empiricalData))
		lastDeltas.append(np.nan)

		optionPrices.extend(map(lambda x: x['optionTick'].last, empiricalData))
		optionPrices.append(np.nan)
		
		stockPrices.extend(map(lambda x: x['underlyingTick'].last, empiricalData))
		stockPrices.append(np.nan)

	stockPrices = pandas.Series(stockPrices)
	optionPrices = pandas.Series(optionPrices)
	lastDeltas = pandas.Series(lastDeltas)
	spreadDeltas = pandas.Series(spreadDeltas)
	timestamps = pandas.tseries.tools.to_datetime(timestamps, unit='ms')


	plotDelta = plots[0]
	plotPrices = plots[1]

	plotDelta.grid(True)
	plotPrices.grid(True)

	plotDeltaSpread = plotDelta
	plotDeltaSpread.scatter(timestamps, spreadDeltas, marker='s', color='k')

	plotDeltaLast = plotDelta.twinx()
	plotDeltaLast.scatter(timestamps, lastDeltas, marker='x', color='g')

	plotOptionPrices = plotPrices
	plotOptionPrices.plot(timestamps, optionPrices, linestyle='-', marker='o', color='b')

	plotStockPrices = plotOptionPrices.twinx()
	plotStockPrices.plot(timestamps, stockPrices, linestyle='-', marker='d', color='r')

	fig.autofmt_xdate(bottom=0.2, rotation=35, ha='right')
	plt.title(instrumentMeta)
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
				profit = computeNakedProfit(pricedData, (1, len(pricedData)-1))
				print 'profit', profit
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






