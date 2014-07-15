

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
                profitRecord['Profit'] = ask_tn - bid_t0
                
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
            profitRecord['Profit'] = (bid_tn - ask_t0) + delta*(underlyingAsk_tn - underlyingBid_t0)
        else:
            profitRecord['Profit'] = (ask_tn - bid_t0) + delta*(underlyingBid_tn - underlyingAsk_t0)
               
        profitRecords.append(profitRecord)
        
        
    return profitRecords