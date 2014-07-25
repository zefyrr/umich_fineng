import numpy as np
import csv

def computeEmpiricals(optionMeta, pricedData, positionIndex):
	(startPositionIndex, endPositionIndex) = positionIndex
        
	empiricalData = []
	#printing values to csv file
	#writer = csv.writer(open('/Users/sindhuramalireddy/Desktop/project/analysis_20140628/code/results/empiricalRecord.csv','wb'))
        #writer.writerow(['Instrument', optionMeta.instrument])
        #writer.writerow(['id', 'deviation', 'deviation with central', 'empirical', 'emp with central', 'theoretical', 'gamma', 'stockLast'])                  		
        #writer.writerow(['id', 'theoretical delta', 'deviation', 'empirical delta'])                  		

	for i in range(startPositionIndex, endPositionIndex-1):
	        pricedRecord_t0 = pricedData[i]
		pricedRecord_t1 = pricedData[i+1]
		#pricedRecord_t2 = pricedData[i+2]

		underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
		underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
		#underlyingTick_t2 = pricedRecord_t2.pairedTick.underlyingTick

		optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
		optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
		#optionTick_t2 = pricedRecord_t2.pairedTick.optionTick
		
		empiricalRecord = {}
		empiricalRecord['timestamp'] = optionTick_t1.timestamp
		empiricalRecord['optionTick'] = optionTick_t1
		empiricalRecord['underlyingTick'] = underlyingTick_t1
		empiricalRecord['underlyingTick'] = underlyingTick_t1
		# empiricalRecord['theoreticals'] = pricedRecord_t0.theoreticals
		empiricalRecord['delta'] = {}


		underlyingLastDiff = (underlyingTick_t0.ask - underlyingTick_t1.ask) + (underlyingTick_t0.bid - underlyingTick_t1.bid)
		optionLastDiff = (optionTick_t0.ask - optionTick_t1.ask) + (optionTick_t0.bid - optionTick_t1.bid)

                #distOne = (underlyingTick_t1.last - underlyingTick_t0.last) 
                #distTwo = (underlyingTick_t2.last - underlyingTick_t1.last)
                
		
		# Skipping deltas that have experienced no change
		if underlyingLastDiff == 0 or optionLastDiff == 0:
			print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (i, i + 1)
			continue

                observedDelta = optionLastDiff/underlyingLastDiff
		empiricalRecord['delta']['spread'] = observedDelta
                

		optionLastDiff = optionTick_t0.last - optionTick_t1.last
		underlyingLastDiff = underlyingTick_t0.last - underlyingTick_t1.last

                observedDelta = optionLastDiff/underlyingLastDiff
		empiricalRecord['delta']['last'] = observedDelta
                
                #opt_t0 = optionTick_t0.last                
                #opt_t1 = optionTick_t1.last
                #opt_t2 = optionTick_t2.last
                
                #observedCentralDelta = (opt_t2 - ((distTwo/distOne)**2)*opt_t0 - (1 - (distTwo/distOne)**2)*opt_t1)/(distTwo*(1 + (distTwo/distOne)))
                #observedGamma = 2*(opt_t2 + (distTwo/distOne)*opt_t2 - (1+(distTwo/distOne))*opt_t1)/(distOne*distTwo*(1 + (distTwo/distOne)))
                #
                #empiricalRecord['delta']['centralDiff'] = observedCentralDelta
                #empiricalRecord['Gamma'] = observedGamma

		empiricalData.append(empiricalRecord)
		
		#writer.writerow(['Timestamp', optionTick_t1.timestampStr])
		deviationList = []
                dict = {}
                for j in range(len(pricedRecord_t1.theoreticals)):
			theoretical = pricedRecord_t1.theoreticals[j]
			dict.update({theoretical.Id.numDataPoints:theoretical.delta})
                        deviation = abs(observedDelta - theoretical.delta)
                        #deviation2 = abs(observedCentralDelta - theoretical.delta)
                       
                        #subDict = {i:j for i,j in dict.iteritems() if deviation < 0.1*observedDelta}
                        #for key, value in subDict.items():
                        #    writer.writerow([key,value, deviation, observedDelta])
                        #writer.writerow('\n')
			deviationList.append({'id': theoretical.Id.numDataPoints, 'deviation': deviation,'empirical': observedDelta, 'theoreticalDelta': theoretical.delta, 'theoreticalPrice': theoretical.price})
                        
		deviationList.sort(key = lambda x: x['deviation'])
		bestList = deviationList[:10]+deviationList[-10:]
		for i in range(len(bestList)):
		    
		#for theoreticalPrice in deviationList[10:] first 10 and last 10
		#  #calculate profit

        return empiricalData
