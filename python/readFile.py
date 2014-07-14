import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import tick_pb2 as proto
import varint
import csv


def getInstrumentIterator(input):
	inputFh = open(input, "rb")
	data  = inputFh.read()
	decoder = varint.decodeVarint32
	next_pos, pos = 0, 0
	# Loop to read each pricedData object in the file

	pricedData = []
	lastOptionMeta = None
	while 1:
		pricedRecord = proto.PricedRecord()

		try:
			next_pos, pos = decoder(data, pos)
		except:
			break
		pricedRecord.ParseFromString(data[pos:pos + next_pos])
		pos += next_pos

		optionMeta = pricedRecord.pairedTick.optionMeta
		if lastOptionMeta:
			if lastOptionMeta.instrument !=  optionMeta.instrument:
				yield (lastOptionMeta, pricedData)
				pricedData = []

		pricedData.append(pricedRecord)
		lastOptionMeta = optionMeta

	inputFh.close()
	yield (lastOptionMeta, pricedData)


def getTimeInSecs(timeStr):
	time = map(lambda x: int(x),  timeStr.split(':'))
	timeSecs = (time[0] * 24 * 60) + (time[1] * 60) + time[2]
	return timeSecs


def createPositions(pricedData):
	positionsIndex = []

	startPositionIndex = None
	endPositionIndex = None

	i = 0
	for pricedRecord in pricedData:
		timeSecs = getTimeInSecs(pricedRecord.pairedTick.optionTick.timestampStr.split(' ')[1])
		
		if not startPositionIndex:
			if timeSecs > getTimeInSecs('09:45:00'):
				startPositionIndex = i

		if not endPositionIndex:
			if timeSecs > getTimeInSecs('15:30:00'):
				endPositionIndex = i
				break

		i = i + 1

	if startPositionIndex and endPositionIndex:
			positionsIndex.append((startPositionIndex, endPositionIndex))

	return positionsIndex

def processPosition(pricedData, positionIndex):
	(startPositionIndex, endPositionIndex) = positionIndex
	for i in range(startPositionIndex, endPositionIndex):
		pricedRecord_t0 = pricedData[i]
		pricedRecord_t1 = pricedData[i+1]
                pricedRecord_t2 = pricedData[i+2]

		underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
		underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
                underlyingTick_t2 = pricedRecord_t2.pairedTick.underlyingTick

		optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
		optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
                optionTick_t2 = pricedRecord_t2.pairedTick.optionTick	           
		  

		underlyingLastDiff = (underlyingTick_t0.ask - underlyingTick_t1.ask) + (underlyingTick_t0.bid - underlyingTick_t1.bid)
		optionLastDiff = (optionTick_t0.ask - optionTick_t1.ask) + (optionTick_t0.bid - optionTick_t1.bid)
		
                #distOne = ((underlyingTick_t1.last - underlyingTick_t0.last) + (underlyingTick_t1.bid - underlyingTick_t0.bid))/2
                #distTwo = ((underlyingTick_t2.ask - underlyingTick_t1.ask) + (underlyingTick_t2.bid - underlyingTick_t1.bid))/2
                
                distOne = (underlyingTick_t1.last - underlyingTick_t0.last) 
                distTwo = (underlyingTick_t2.last - underlyingTick_t1.last)

                #underlyingcentraldiff = 
                #optioncentraldiff = 

		# underlyingLastDiff = underlyingTick_t0.last - underlyingTick_t1.last
		# optionLastDiff = optionTick_t0.last - optionTick_t1.last

		# Skipping deltas that have experienced no change
		if underlyingLastDiff == 0 or optionLastDiff == 0:
			print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (i, i + 1)
			continue

                if distOne == 0 or distTwo == 0:
			print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (i, i + 1)
			continue

		observedDelta = optionLastDiff/underlyingLastDiff
                
                #opt_t0 = (optionTick_t0.ask + optionTick_t0.bid)/2                
                #opt_t1 = (optionTick_t1.ask + optionTick_t1.bid)/2
                #opt_t2 = (optionTick_t2.ask + optionTick_t2.bid)/2

                opt_t0 = optionTick_t0.last                
                opt_t1 = optionTick_t1.last
                opt_t2 = optionTick_t2.last
                
                observedCentralDelta = (opt_t2 - ((distTwo/distOne)**2)*opt_t0 - (1 - (distTwo/distOne)**2)*opt_t1)/(distTwo*(1 + (distTwo/distOne)))
                #observedCentralDelta2 = ((-distTwo)/((distOne)*(distOne + distTwo)))*opt                            

                observedGamma = 2*(opt_t2 + (distTwo/distOne)*opt_t2 - (1+(distTwo/distOne))*opt_t1)/(distOne*distTwo*(1 + (distTwo/distOne)))
                
                
                writer = csv.writer(open('sankethlist.csv','wb'))
                writer.writerow(['id', 'deviation', 'deviation with central', 'empirical', 'emp with central', 'theoretical', 'gamma', 'stockLast'])                  		
                #deviationList = []
                deviationList = []
		for j in range(len(pricedRecord_t0.theoreticals)):
			theoretical = pricedRecord_t0.theoreticals[j]
			
			
			deviation = abs(observedDelta - theoretical.delta)
                        deviation2 = abs(observedCentralDelta - theoretical.delta)

			deviationList.append({'id': theoretical.Id.numDataPoints, 'deviation': deviation, 'deviation with central': deviation2, 'empirical': observedDelta, 'emp with central': observedCentralDelta, 'theoretical': theoretical.delta, 'stockLast': underlyingTick_t0.last})
                        writer.writerow([theoretical.Id.numDataPoints, deviation, deviation2, observedDelta, observedCentralDelta, theoretical.delta, observedGamma, underlyingTick_t0.last])
			#theoreticalPrice = theoretical.price
		deviationList.sort(key = lambda x: x['deviation with central'])

		print deviationList[:10]




def processInstrument(optionMeta, pricedData):
	print 'Processing -', optionMeta

	positions = createPositions(pricedData)
	if len(positions) == 0:
		print 'No positions found'
		return 

	for positionIndex in positions:
		processPosition(pricedData, positionIndex)



def main():
    #parser = argparse.ArgumentParser(description="Run analysis")
    #parser.add_argument('-d', '--datadir', help='location of priced data')

    #args = parser.parse_args()
    
#    if not args.datadir:
#    	parser.print_help()
#    	return
#
#    if not os.path.exists(args.datadir):
#    	print 'Invalid path %s' % args.datadir
#    	return
    
    print 'check'
    for root, dirnames, filenames in os.walk("C://Trading//data//analysis_20140628//FDX.priced//FDX//FDX//20140610"):
    	for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
    		pricedDataFile = root + "//" + filename
    		print 'Processing file -', pricedDataFile 
    		for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile):
    			processInstrument(optionMeta, pricedData)

 


if __name__ == "__main__":
    main()