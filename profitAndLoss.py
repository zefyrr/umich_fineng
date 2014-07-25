

def computeNakedProfit(pricedData, positionIndex):
    pricedRecord_t0 = pricedData[positionIndex[0]]    #entry position
    pricedRecord_tn = pricedData[positionIndex[1]]  #exit position
    
    marketPrice = pricedRecord_t0.pairedTick.optionTick.last
    bid_t0 = pricedRecord_t0.pairedTick.optionTick.bid
    ask_t0 = pricedRecord_t0.pairedTick.optionTick.ask
    bid_tn = pricedRecord_tn.pairedTick.optionTick.bid
    ask_tn = pricedRecord_tn.pairedTick.optionTick.ask
    
    
    profitRecords = []	
    
    for theoretical in pricedRecord_t0.theoreticals:
        theoreticalPrice = theoretical.price
        index_t0 = theoretical.Id.numDataPoints
        profitRecord = {}
        profitRecord['StartPositionIndex'] = index_t0
        if theoreticalPrice > marketPrice:
                profitRecord['Profit'] = bid_tn - ask_t0
                
        else:
                profitRecord['Profit'] = bid_t0 - ask_tn
                
        profitRecords.append(profitRecord)
        
    return profitRecords
                
def computeHedgedProfit(pricedData, positionIndex):
    
    pricedRecord_t0 = pricedData[positionIndex[0]]    #entry position
    pricedRecord_tn = pricedData[positionIndex[1]]  #exit position
    
    marketPrice = pricedRecord_t0.pairedTick.optionTick.last
    bid_t0 = pricedRecord_t0.pairedTick.optionTick.bid
    ask_t0 = pricedRecord_t0.pairedTick.optionTick.ask
    bid_tn = pricedRecord_tn.pairedTick.optionTick.bid
    ask_tn = pricedRecord_tn.pairedTick.optionTick.ask
    underlyingBid_t0 = pricedRecord_t0.pairedTick.underlyingTick.bid
    underlyingAsk_t0 = pricedRecord_t0.pairedTick.underlyingTick.ask
    underlyingBid_tn = pricedRecord_tn.pairedTick.underlyingTick.bid
    underlyingAsk_tn = pricedRecord_tn.pairedTick.underlyingTick.ask
    
    profitRecords = []
    
    for theoretical in pricedRecord_t0.theoreticals:
        theoreticalPrice = theoretical.price
        index_t0 = theoretical.Id.numDataPoints
        delta = theoretical.delta
        
        profitRecord = {}
        profitRecord['StartPositionIndex'] = index_t0
                
        if theoreticalPrice > marketPrice:
            profitRecord['Profit'] = (bid_tn - ask_t0) - delta*(underlyingAsk_tn - underlyingBid_t0)
        else:
            profitRecord['Profit'] = (bid_t0 - ask_tn) + delta*(underlyingBid_tn - underlyingAsk_t0)
               
        profitRecords.append(profitRecord)
        
        
    return profitRecords
    
def NakedProfitPerPosition(optionMeta, pricedData, positionIndex):
        (startPositionIndex, endPositionIndex) = positionIndex
        
	#printing values to csv file
	#writer = csv.writer(open('/Users/sindhuramalireddy/Desktop/project/analysis_20140628/code/results/empiricalRecord.csv','wb'))
        #writer.writerow(['Instrument', optionMeta.instrument])
        #writer.writerow(['id', 'deviation', 'deviation with central', 'empirical', 'emp with central', 'theoretical', 'gamma', 'stockLast'])                  		
        #writer.writerow(['id', 'theoretical delta', 'deviation', 'empirical delta'])                  		

	pricedRecord_t0 = pricedData[startPositionIndex]
	pricedRecord_t1 = pricedData[startPositionIndex+1]
	pricedRecord_tn = pricedData[endPositionIndex]
		
	underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
	underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
	
	optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
	optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
		
	marketPrice = pricedRecord_t1.pairedTick.optionTick.last
        bid_t1 = pricedRecord_t1.pairedTick.optionTick.bid
        ask_t1 = pricedRecord_t1.pairedTick.optionTick.ask
        bid_tn = pricedRecord_tn.pairedTick.optionTick.bid
        ask_tn = pricedRecord_tn.pairedTick.optionTick.ask
        
	profitRecord = {}
	profitRecord['timestamp'] = optionTick_t1.timestamp
	profitRecord['optionTick'] = optionTick_t1
	profitRecord['underlyingTick'] = underlyingTick_t1
	# empiricalRecord['theoreticals'] = pricedRecord_t1.theoreticals

        optionLastDiff = optionTick_t0.last - optionTick_t1.last
	underlyingLastDiff = underlyingTick_t0.last - underlyingTick_t1.last
        #if underlyingLastDiff == 0 or optionLastDiff == 0:
        #    print "delta nan"
        #    continue

        observedDelta = optionLastDiff/underlyingLastDiff
	profitRecord['delta'] = observedDelta
        	
	#writer.writerow(['Timestamp', optionTick_t1.timestampStr])
	deviationList = []
        dict = {}
        for j in range(len(pricedRecord_t1.theoreticals)):
			theoretical = pricedRecord_t1.theoreticals[j]
			dict.update({theoretical.Id.numDataPoints:theoretical.delta})
                        deviation = observedDelta - theoretical.delta
                        deviationList.append({'id': theoretical.Id.numDataPoints, 'deviation': deviation,'empirical': observedDelta, 'theoreticalDelta': theoretical.delta, 'theoreticalPrice': theoretical.price})
                        
	deviationList.sort(key = lambda x: x['deviation'])
	bestList = deviationList[:10]+deviationList[-10:]
	profitRecord['Profit']={}
	for i in range(len(bestList)):
	        if deviationList[i].get('theoreticalPrice') > marketPrice:
                    profitRecord['Profit'][bestList[i].get('id')] = bid_tn - ask_t1
                else:
                    profitRecord['Profit'][bestList[i].get('id')] = bid_t1 - ask_tn
                    
        return profitRecord
        
def HedgedProfitPerPosition(optionMeta, pricedData, positionIndex):
        (startPositionIndex, endPositionIndex) = positionIndex
        
	#printing values to csv file
	#writer = csv.writer(open('/Users/sindhuramalireddy/Desktop/project/analysis_20140628/code/results/empiricalRecord.csv','wb'))
        #writer.writerow(['Instrument', optionMeta.instrument])
        #writer.writerow(['id', 'deviation', 'deviation with central', 'empirical', 'emp with central', 'theoretical', 'gamma', 'stockLast'])                  		
        #writer.writerow(['id', 'theoretical delta', 'deviation', 'empirical delta'])                  		

	pricedRecord_t0 = pricedData[startPositionIndex]
	pricedRecord_t1 = pricedData[startPositionIndex+1]
	pricedRecord_tn = pricedData[endPositionIndex]
		
	underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
	underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
	
	optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
	optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
		
	marketPrice = pricedRecord_t1.pairedTick.optionTick.last
        bid_t1 = pricedRecord_t1.pairedTick.optionTick.bid
        ask_t1 = pricedRecord_t1.pairedTick.optionTick.ask
        bid_tn = pricedRecord_tn.pairedTick.optionTick.bid
        ask_tn = pricedRecord_tn.pairedTick.optionTick.ask
        underlyingBid_t1 = pricedRecord_t1.pairedTick.underlyingTick.bid
        underlyingAsk_t1 = pricedRecord_t1.pairedTick.underlyingTick.ask
        underlyingBid_tn = pricedRecord_tn.pairedTick.underlyingTick.bid
        underlyingAsk_tn = pricedRecord_tn.pairedTick.underlyingTick.ask
        
	profitRecord = {}
	profitRecord['timestamp'] = optionTick_t1.timestamp
	profitRecord['optionTick'] = optionTick_t1
	profitRecord['underlyingTick'] = underlyingTick_t1
	# empiricalRecord['theoreticals'] = pricedRecord_t1.theoreticals

        optionLastDiff = optionTick_t0.last - optionTick_t1.last
	underlyingLastDiff = underlyingTick_t0.last - underlyingTick_t1.last
        #if underlyingLastDiff == 0 or optionLastDiff == 0:
        #    print "delta nan"
        #    continue

        observedDelta = optionLastDiff/underlyingLastDiff
	profitRecord['delta'] = observedDelta
        	
	#writer.writerow(['Timestamp', optionTick_t1.timestampStr])
	deviationList = []
        dict = {}
        for j in range(len(pricedRecord_t1.theoreticals)):
			theoretical = pricedRecord_t1.theoreticals[j]
			dict.update({theoretical.Id.numDataPoints:theoretical.delta})
                        deviation = observedDelta - theoretical.delta
                        deviationList.append({'id': theoretical.Id.numDataPoints, 'deviation': deviation,'empirical': observedDelta, 'theoreticalDelta': theoretical.delta, 'theoreticalPrice': theoretical.price})
                        
	deviationList.sort(key = lambda x: x['deviation'])
	bestList = deviationList[:10]+deviationList[-10:]
	profitRecord['Profit']={}
	for i in range(len(bestList)):
	        delta = deviationList[i].get('theoreticalDelta')
	        if deviationList[i].get('theoreticalPrice') > marketPrice:
                    profitRecord['Profit'][bestList[i].get('id')] = (bid_tn - ask_t1) - delta*(underlyingAsk_tn - underlyingBid_t1)
                else:
                    profitRecord['Profit'][bestList[i].get('id')] = (bid_t1 - ask_tn) + delta*(underlyingBid_tn - underlyingAsk_t1)
                    
        return profitRecord