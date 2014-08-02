import numpy as np
import math

def computeMinMax(optionMeta, pricedData, positionIndex):

	(startPosition, endPosition)  = positionIndex

	startPricedRecord = pricedData[startPosition]
	mktPrice = startPricedRecord.pairedTick.optionTick.last

	maxDrawDowns = []
	for theoreticalRecord in startPricedRecord.theoreticals:
		if math.isnan(theoreticalRecord.price):
			continue
		if math.isnan(theoreticalRecord.delta):
			continue

		direction = 1 if theoreticalRecord.price >= mktPrice else -1

		prices = []
		for i in range(startPosition, endPosition):		
			pricedRecord = pricedData[i]

			optionPrice = pricedRecord.pairedTick.optionTick.last
			underlyingPrice = pricedRecord.pairedTick.underlyingTick.last

			positionValue = direction * (optionPrice - (underlyingPrice * theoreticalRecord.delta))
			prices.append(positionValue)

		drawDowns = computeDrawDowns(prices)
		maxDrawDown = max(drawDowns, key=lambda x: x['drawdown'])
		maxDrawDown['theoretical'] = theoreticalRecord
		maxDrawDowns.append(maxDrawDown)


	minMaxdrawDown = min(maxDrawDowns, key=lambda x: x['drawdown'])
	minMaxdrawDown['start'] = pricedData[maxDrawDown['start'] + startPosition].pairedTick.underlyingTick.timestampStr
	minMaxdrawDown['end'] = pricedData[maxDrawDown['end'] + startPosition].pairedTick.underlyingTick.timestampStr
	return minMaxdrawDown




def computeDrawDowns(prices):
	runningMax = prices[0]
	maxIndex = 0
	drawdowns = []
	for i in range(1, len(prices)):
		currentPrice = prices[i]
		drawdown = runningMax - currentPrice
		if drawdown > 0:
			drawdowns.append({'drawdown': drawdown, 'start': maxIndex, 'end': i})
		if runningMax <  currentPrice:
			runningMax = currentPrice
			maxIndex = i
	return drawdowns


