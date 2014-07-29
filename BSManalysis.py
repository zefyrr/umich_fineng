#BLack Scholes Model
#BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], volatility=x, callPrice=y, putPrice=z)
import mibian
import pandas as pd

def computeBSMValues(optionMeta, pricedData):
    BSMdata = []
    for pricedRecord in pricedData:
        underlyingPrice = (pricedRecord.pairedTick.underlyingTick.bid + pricedRecord.pairedTick.underlyingTick.ask)/2
        callPrice = (pricedRecord.pairedTick.optionTick.bid + pricedRecord.pairedTick.optionTick.ask)/2
        interestRate = pricedRecord.pairedTick.interestRate 
        daysToExpiration = pricedRecord.pairedTick.daysToExpire
        strikePrice = pricedRecord.pairedTick.optionMeta.strike
        
        c = mibian.BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], callPrice=callPrice)
        impVol = c.impliedVolatility
        
        c = mibian.BS([underlyingPrice, strikePrice, interestRate, daysToExpiration], volatility = impVol)
        BSdelta = c.callDelta
        BSprice = c.callPrice
        theoDelta = []
        theoPrice = []
        for theoretical in pricedRecord.theoreticals:
            theoDelta.append(theoretical.delta)
            theoPrice.append(theoretical.price)
        BSMdata.append({'Timestamp' : pricedRecord.pairedTick.optionTick.timestamp,
                        'Instrument': optionMeta.instrument,
                        'OptionPrice': callPrice,
                        'UnderlyingPrice': underlyingPrice,
                        'BSMdelta': BSdelta,
                        'TheoreticalDeltaMin':min(theoDelta),
                        'TheoreticalDeltaMax':max(theoDelta),
                        'BSMprice' : BSprice,
                        'TheoreticalPriceMin': min(theoPrice),
                        'TheoreticalPriceMax': max(theoPrice) 
                        })
        
    BSMdf = pd.DataFrame.from_dict(BSMdata,orient="columns",dtype=None)
    return BSMdf
        
        
        