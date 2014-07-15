from utils import getTimeInSecs

def createPositions(pricedData):
	positionsIndex = []

	startPositionIndex = None
	endPositionIndex = None

	i = 0
	for pricedRecord in pricedData:
		timeSecs = getTimeInSecs(pricedRecord.pairedTick.optionTick.timestampStr.split(' ')[1])
		
		if not startPositionIndex:
			if timeSecs > getTimeInSecs('09:10:00'):
				startPositionIndex = i

		if not endPositionIndex:
			if timeSecs > getTimeInSecs('15:30:00'):
				endPositionIndex = i
				break

		i = i + 1

	if startPositionIndex and endPositionIndex:
			positionsIndex.append((startPositionIndex, endPositionIndex))

	return positionsIndex
