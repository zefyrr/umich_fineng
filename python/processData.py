import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import matplotlib.pyplot as plt
import math, pandas
import time
from readProto import getInstrumentIterator
from utils import getTimeGMTFromUTCEpoch, getTimeInSecs
from empiricalDelta import computeDeltas
import itertools




def processInstrument(optionMeta, pricedData):

	instrumentMeta = '%s %f %s' % (optionMeta.instrument, optionMeta.strike, getTimeGMTFromUTCEpoch(optionMeta.expirationDate))

	print 'Processing -', instrumentMeta, 'ticks -', len(pricedData)
	firstPricedRecord = pricedData[0]

	if len(pricedData) <= 8:
		#print 'Not enough ticks'
		return 

	empiricals = computeDeltas(pricedData, (0, len(pricedData) - 1), useSpread=False)

	timestamps = map(lambda x: x[0], empiricals)
	timestamps = pandas.tseries.tools.to_datetime(timestamps, unit='ms')

	deltas = pandas.Series(map(lambda x: x[1], empiricals))
	optionPrices = pandas.Series(map(lambda x: x[2], empiricals))
	stockPrices = pandas.Series(map(lambda x: x[3], empiricals))

	return (instrumentMeta, timestamps, deltas, optionPrices, stockPrices)




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

	instrumentMetaMap = {}
	for root, dirnames, filenames in os.walk(args.datadir):
		for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
			pricedDataFile = root + "/" + filename
			print 'Processing file -', pricedDataFile 

			for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile):
				processedData = processInstrument(optionMeta, pricedData)
				if processedData:
					(instrumentMeta, timestamps, deltas, optionPrices, stockPrices) = processedData
					instrumentMetaData = instrumentMetaMap.get(instrumentMeta, [])
					instrumentMetaData.append((timestamps, deltas, optionPrices, stockPrices))
					instrumentMetaMap[instrumentMeta] = instrumentMetaData

	for instrumentMeta in instrumentMetaMap.keys():
		instrumentMetaData = instrumentMetaMap.get(instrumentMeta, [])
		timestamps = list(itertools.chain(*map(lambda x: x[0], instrumentMetaData)))
		deltas = list(itertools.chain(*map(lambda x: x[1], instrumentMetaData)))
		optionPrices = list(itertools.chain(*map(lambda x: x[2], instrumentMetaData)))
		stockPrices = list(itertools.chain(*map(lambda x: x[3], instrumentMetaData)))
		fig, axarr = plt.subplots(2, sharex=True)
		axarr[0].scatter(timestamps, deltas)
		axarr[1].plot(timestamps, optionPrices, linestyle='-', marker='o', color='b')
		axarr[0].grid(True)
		axarr[1].grid(True)
		stockPlot = axarr[1].twinx()
		stockPlot.plot(timestamps, stockPrices, linestyle='-', marker='d', color='r')
		plt.title(instrumentMeta)
		fig.autofmt_xdate()
		plt.show()

		if raw_input("Press 'q' to quit\n").lower() == 'q':
			return


if __name__ == "__main__":
    main()






