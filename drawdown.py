#drawdowns

#Method2
def dd2(optionMeta, pricedData, positionIndex):
    OptPrice = []
    for i in range(positionIndex):
        pricedRecord = pricedData[i]
        OptPrice.append(pricedRecord.pairedTick.optionTick.last)
    
    runningMax = [max(OptPrice[:i]) for i in range(1,len(OptPrice)+1)]
    drawdowns = runningMax - OptPrice
    return max(drawdowns)
    
