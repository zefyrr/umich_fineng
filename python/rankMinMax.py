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


def createPositions(pricedData):
	positionsIndex = []

	startPositionIndex = None
	endPositionIndex = None

	i = 0
	for pricedRecord in pricedData:
		timeSecs = getTimeInSecs(pricedRecord.pairedTick.optionTick.timestampStr.split(' ')[1])
		
		if not startPositionIndex:
			if timeSecs > getTimeInSecs('09:30:00'):
				startPositionIndex = i

		if not endPositionIndex:
			if timeSecs > getTimeInSecs('15:30:00'):
				endPositionIndex = i
				break

		i = i + 1

	if startPositionIndex and endPositionIndex:
			positionsIndex.append((startPositionIndex, endPositionIndex))

	return positionsIndex


def computeStats(startPricedRecord):
	pairedTick = startPricedRecord.pairedTick
	daysToExpire = pairedTick.daysToExpire
	strike = pairedTick.optionMeta.strike
	expirationDate = getDateGMTFromUTCEpoch(pairedTick.optionMeta.expirationDate)
	last = pairedTick.underlyingTick.last
	instrument = pairedTick.optionMeta.instrument
	tradingDay = pairedTick.underlyingTick.timestampStr[0:10]
	return (tradingDay, instrument, strike, expirationDate, daysToExpire, last/strike)

def computeProfitLoss(pricedData, minMax, position):
	startIndex, endIndex = position

	theoretical = minMax['theoretical']
	direction = minMax['direction']
	positionType = "Buy" if direction == 1 else "Sell"
	numDataPoints = theoretical.Id.numDataPoints
	delta = theoretical.delta
	price = theoretical.price


	prices = []
	for i in range(startIndex, endIndex):		
		pricedRecord = pricedData[i]

		optionPrice = pricedRecord.pairedTick.optionTick.last
		underlyingPrice = pricedRecord.pairedTick.underlyingTick.last
		positionValue = (direction * (optionPrice - (underlyingPrice * delta))) * 100

		prices.append(positionValue)

	profit = prices[-1] - prices[0]
	return theoretical.Id.numDataPoints, profit, minMax['drawdown']



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

	statsFh = open('rank.stats.tsv', 'w')
	header = []
	header.extend(['tradingDay'])
	header.extend(['instrument', 'strike', 'expirationDate'])
	header.extend(['daysToExpire', 's/x'])
	header.extend(['rank'])
	header.extend(['numDataPoints', 'p/l', 'drawDown'])

	statsFh.write('\t'.join(header))
	statsFh.write('\n')

	for root, dirnames, filenames in os.walk(args.datadir):
		for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
			pricedDataFile = root + "/" + filename
			print 'Processing file -', pricedDataFile 


			for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile):
				if len(pricedData) <= 8:
					print 'Not enough ticks\n', optionMeta
					continue
				else:
					print 'Processing\n', optionMeta


				for position in createPositions(pricedData):
					startPosition, endPosition = position
					stats = computeStats(pricedData[startPosition])

					topKMinMax = computeMinMax(pricedData, position)
					if not topKMinMax:
						continue
					i = 0
					for minMax in topKMinMax:
						metrics = computeProfitLoss(pricedData, minMax, position)
						output = []
						i = i + 1
						output.extend(stats)
						output.append(i)
						output.extend(metrics)
						output = map(lambda x: str(x), output)
						statsFh.write('\t'.join(output))
						statsFh.write('\n')
						statsFh.flush()
	statsFh.close()



if __name__ == "__main__":
    main()






