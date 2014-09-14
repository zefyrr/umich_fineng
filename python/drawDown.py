import numpy as np
import math




def computeMinMax(pricedData, positionIndex, topK = 5):

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
		if len(drawDowns) == 0:
			continue

		maxDrawDown = max(drawDowns, key=lambda x: x['drawdown'])
		maxDrawDown['theoretical'] = theoreticalRecord
		maxDrawDown['direction'] = direction
		maxDrawDowns.append(maxDrawDown)

	if len(maxDrawDowns) == 0:
		return

	sortedMaxdrawDowns = sorted(maxDrawDowns, key=lambda x: x['drawdown'])
	topK_DrawDowns = sortedMaxdrawDowns[:topK]
	for minMaxdrawDown in topK_DrawDowns:
		minMaxdrawDown['start'] = maxDrawDown['start'] + startPosition
		minMaxdrawDown['end'] = maxDrawDown['end'] + startPosition
	return topK_DrawDowns




def computeDrawDowns(prices):
	startPrice = prices[0]
	runningMax = startPrice
	maxIndex = 0
	drawdowns = []
	for i in range(1, len(prices)):
		currentPrice = prices[i]
		drawdown = (runningMax - currentPrice)/float(runningMax)
		if drawdown > 0:
			drawDown_relative = drawdown/startPrice
			drawDown_regime = None
			if currentPrice < startPrice:
				drawDown_regime = 'loss'
			else:
				drawDown_regime = 'profit'

			drawDownDict = {}
			drawDownDict['drawdown'] = drawdown
			drawDownDict['start'] = maxIndex
			drawDownDict['end'] = i
			drawDownDict['drawDown_relative'] = drawDown_relative
			drawDownDict['drawDown_regime'] = drawDown_regime
			drawdowns.append(drawDownDict)
			
		if runningMax < currentPrice:
			runningMax = currentPrice
			maxIndex = i
	return drawdowns


