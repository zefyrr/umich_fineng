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


	for root, dirnames, filenames in os.walk(args.datadir):
		for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
			pricedDataFile = root + "/" + filename

			instrumentMetaMap = {}
			for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile):
				for pricedRecord in pricedData:
					instrumentMeta = getInstrumentMetaStr(pricedRecord.pairedTick.optionMeta)
					instrumentMetaMap[instrumentMeta] = instrumentMetaMap.get(instrumentMeta, 0) + 1

			for key, value in  instrumentMetaMap.items():
				print "%s - %d" % (key, value)


if __name__ == "__main__":
    main()






