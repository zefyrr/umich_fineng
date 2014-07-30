#drawdowns
import pandas as pd
import numpy as np

def computeDD(optionMeta, pricedData, positionIndex):
    
    theoData = []
    pricedRecord_t0 = pricedData[positionIndex[0]]
    mktPrice = pricedRecord_t0.pairedTick.optionTick.last
    #adding all theoreticals to a dataframe
    for theoretical in pricedRecord_t0.theoreticals:
        theoData.append({'Index':theoretical.Id.numDataPoints,
                             'Price': theoretical.price,
                             'Delta': theoretical.delta
                            })
    theoDF = pd.DataFrame.from_dict(theoData,orient="columns",dtype=None)
    
    theoDataBuy = theoDF.loc[theoDF['Price'] >= mktPrice]
    theoDataSell = theoDF.loc[theoDF['Price'] < mktPrice]
    theoSet = theoDataSell
    position = -1   #Sell
    if (len(theoDataBuy.index) > len(theoDataSell.index)):
        theoSet = theoDataBuy
        position = 1    #Buy
    
    ddPerDelta = []
    for index, row in theoSet.iterrows():
        assetValues = []
        delta = row['Delta']
        for i in range(positionIndex[0],positionIndex[1]):
            pricedRecord = pricedData[i]
            optPrice = pricedRecord.pairedTick.optionTick.last
            underlyingPrice = pricedRecord.pairedTick.underlyingTick.last
            assetValues.append(position*(optPrice - (underlyingPrice * delta)))
        ddPerDelta.append({'Index':row['Index'],
                           'Drawdown':getDD(assetValues)
                           }) 
    ddPerDeltaDF = pd.DataFrame.from_dict(ddPerDelta,orient="columns",dtype=None)
    return ddPerDeltaDF.sort(columns = 'Drawdown')
  

      
def getDD(assetValues):
    runningMax = [max(assetValues[:i]) for i in range(1,len(assetValues)+1)]
    drawdowns =  np.subtract(runningMax,assetValues)
    return max(drawdowns)
    
