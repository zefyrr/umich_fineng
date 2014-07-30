import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import matplotlib.pyplot as plt
import math, pandas
import time
from readProto import getInstrumentIterator
from utils import getTimeGMTFromUTCEpoch, getTimeInSecs, getInstrumentMetaStr
import itertools
import numpy as np
from profitAndLoss import *
from positions import createPositions
from BSManalysis import *
from drawdown import *


def processInstrument(optionMeta, pricedData):

	instrumentMeta = '%s %f %s' % (optionMeta.instrument, optionMeta.strike, getTimeGMTFromUTCEpoch(optionMeta.expirationDate))

	print 'Processing -', instrumentMeta, 'ticks -', len(pricedData)
	
	if len(pricedData) <= 8:
		'Not enough ticks'
		return 
		
	positions = createPositions(pricedData)
	#raw_input('in process instrument')
	if len(positions) == 0:
		print 'No positions found'
		return 

	#for positionIndex in positions:
	#	#Naked profit
	#	profitRecord = NakedProfitPerPosition(optionMeta, pricedData, positionIndex)
	#	#writer1 = csv.writer(open("./nakedProfit.csv",'wb'))
	#	#writer.writerow()
	#	##HEdged Profit
	#	profitRecord = HedgedProfitPerPosition(optionMeta, pricedData, positionIndex)
	#	#writer2 = csv.writer(open("./nakedProfit.csv",'wb'))
	#	print profitRecord
	#	break
	#	return profitRecord

        for positionIndex in positions:
            print "pos", positionIndex
            dd = computeDD(optionMeta, pricedData, positionIndex)
            print dd
            break
	#return computeEmpiricals(optionMeta, pricedData, (0, len(pricedData)-1))
	


# class PointBrowser:
#     def __init__(self, ):




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

			for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile,('FDX1421F145')):
				instrumentMeta = getInstrumentMetaStr(optionMeta)
				print 'Processing instrument - ', instrumentMeta
				processedData = processInstrument(optionMeta, pricedData)
				#profit = computeNakedProfit(pricedData, (1, len(pricedData)-1))
				#print 'profit', profit
				#BSMdata = computeBSMValues(optionMeta,pricedData)
				#print "BSM", BSMdata

	        if raw_input("Press 'q' and then enter to quit, or enter to continue\n").lower() == 'q':
			return


if __name__ == "__main__":
    main()






