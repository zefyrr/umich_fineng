import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import time
from readProto import getInstrumentIterator
from utils import getDateGMTFromUTCEpoch, getTimeInSecs, getInstrumentMetaStr
import itertools





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

	fh = open('data.tsv', 'w')

	processedDataMap = {}
	for root, dirnames, filenames in os.walk(args.datadir):
		for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
			pricedDataFile = root + "/" + filename
			print 'Processing file -', pricedDataFile 

			for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile, ('FDX1421F145')):
				for pricedRecord in pricedData:
					underlyingTick = pricedRecord.pairedTick.underlyingTick
					optionTick = pricedRecord.pairedTick.optionTick

					fields = optionTick.timestampStr, optionTick.last, underlyingTick.last
					fields = map(lambda x: str(x), fields)

					print '\t'.join(fields)
					fh.write('\t'.join(fields))
					fh.write('\n')


	fh.close

if __name__ == "__main__":
    main()






