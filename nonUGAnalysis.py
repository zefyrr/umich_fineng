#author: Sanketh
from utils import getTimeInSecs
import pandas as pd

def nonUniformGridAnalysis(pricedData,optionMeta, positionIndex):
    nonUniGridData = []
    counter = 0            
    for p in range(positionIndex[0],positionIndex[1] + 1):
        observedDelta = 0
        callPrice = 0
        underlyingPrice = 0
        observedGamma = 0
        timeSecsCurrent = getTimeInSecs(pricedData[p].pairedTick.optionTick.timestampStr.split(' ')[1])
        timeSecsPrevious = getTimeInSecs(pricedData[p-1].pairedTick.optionTick.timestampStr.split(' ')[1])
        timeDiff = timeSecsCurrent-timeSecsPrevious
        if timeDiff < getTimeInSecs('00:05:00'):
                counter = counter + 1
        else:
                if counter == 1:                    
                    pricedRecord_t0 = pricedData[counter-1]
                    pricedRecord_t1 = pricedData[counter]
                    prpRecord = pricedRecord_t1

                    underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
                    underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
                
                    optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
                    optionTick_t1 = pricedRecord_t1.pairedTick.optionTick

                    underlyingLastDiff = ((underlyingTick_t1.ask + underlyingTick_t1.bid)/2 - (underlyingTick_t0.ask + underlyingTick_t0.bid)/2)
                    optionLastDiff = ((optionTick_t1.ask + optionTick_t1.bid)/2 - (optionTick_t0.ask + optionTick_t0.bid)/2)

                    if underlyingLastDiff == 0 or optionLastDiff == 0:
                        print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (p, p + 1)
                        continue

   #                 if distOne == 0 or distTwo == 0:
			#print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (i, i + 1)
			#continue

                    observedDelta = optionLastDiff/underlyingLastDiff
                    #observedGamma = 
                    underlyingPrice = pricedRecord_t1.pairedTick.underlyingTick.last
                    callPrice = pricedRecord_t1.pairedTick.optionTick.last
                    #interestRate = pricedRecord_t1.pairedTick.interestRate 
                    #daysToExpiration = pricedRecord_t1.pairedTick.daysToExpire
                    #strikePrice = pricedRecord_t1.pairedTick.optionMeta.strike
                else: 
                    #if counter >= 2:    DONT need this condition
                    pricedRecord_t0 = pricedData[counter-2]
                    pricedRecord_t1 = pricedData[counter-1]
                    pricedRecord_t2 = pricedData[counter]
                    prpRecord = pricedRecord_t2
                    underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
                    underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
                    underlyingTick_t2 = pricedRecord_t2.pairedTick.underlyingTick

                    optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
                    optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
                    optionTick_t2 = pricedRecord_t2.pairedTick.optionTick

                    a = ((underlyingTick_t2.ask + underlyingTick_t2.bid)/2 - (underlyingTick_t1.ask + underlyingTick_t1.bid)/2)
                    b = ((underlyingTick_t2.ask + underlyingTick_t2.bid)/2 - (underlyingTick_t0.ask + underlyingTick_t0.bid)/2)
                        
                                             
                    denominator = (a*b*(b-a))
                    numerator = (pow(a,2)*(optionTick_t0.ask + optionTick_t0.bid)/2 - pow(b,2)*(optionTick_t1.ask + optionTick_t1.bid)/2 + (pow(b,2) - pow(a,2))*(optionTick_t2.ask + optionTick_t2.bid)/2)

                    if numerator == 0 or denominator == 0:
                            print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (p, p + 1)
                            continue
                       
                    observedDelta = numerator/denominator
                                                
                    observedGamma = ((-a*(optionTick_t0.ask + optionTick_t0.bid)/2 + b*(underlyingTick_t1.ask + underlyingTick_t1.bid)/2 - (b-a)*(optionTick_t2.ask + optionTick_t2.bid)/2)*-2)/denominator
                    underlyingPrice = pricedRecord_t2.pairedTick.underlyingTick.last
                    callPrice = pricedRecord_t2.pairedTick.optionTick.last
                    #interestRate = pricedRecord_t2.pairedTick.interestRate 
                    #daysToExpiration = pricedRecord_t2.pairedTick.daysToExpire
                    #strikePrice = pricedRecord_t2.pairedTick.optionMeta.strike

        nonUniGridData.append({'Timestamp' : prpRecord.pairedTick.optionTick.timestamp,
                               'Instrument': optionMeta.instrument,
                               'OptionPrice': callPrice,
                               'UnderlyingPrice': underlyingPrice,
                               'NUGdelta': observedDelta,
                               })
    
    nonUGdf = pd.DataFrame.from_dict(nonUniGridData,orient="columns",dtype=None)
    return nonUGdf