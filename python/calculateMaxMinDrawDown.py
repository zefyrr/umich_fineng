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
from positions import createPositions
from drawDown import computeMinMax
import pprint
pp = pprint.PrettyPrinter(indent=2)

def processInstrument(optionMeta, pricedData):
	instrumentMeta = getInstrumentMetaStr(optionMeta)
	print 'Processing -', instrumentMeta, 'ticks -', len(pricedData)

	if len(pricedData) <= 8:
		'Not enough ticks'
		return 

	positions = createPositions(pricedData)
	for position in positions:
		minMax = computeMinMax(optionMeta, pricedData, position)
		pp.pprint(minMax) 
		print minMax['theoretical']



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
				instrumentMeta = getInstrumentMetaStr(optionMeta)
				processedData = processInstrument(optionMeta, pricedData)





if __name__ == "__main__":
    main()






