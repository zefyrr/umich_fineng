import numpy as np


def computeEmpiricals(pricedData, positionIndex):
	(startPositionIndex, endPositionIndex) = positionIndex

	empiricalData = []
	for i in range(startPositionIndex, endPositionIndex):
		pricedRecord_t0 = pricedData[i]
		pricedRecord_t1 = pricedData[i+1]

		underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
		underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick

		optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
		optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
		
		empiricalRecord = {}
		empiricalRecord['timestamp'] = optionTick_t1.timestamp
		empiricalRecord['optionTick'] = optionTick_t1
		empiricalRecord['underlyingTick'] = underlyingTick_t1
		empiricalRecord['underlyingTick'] = underlyingTick_t1
		empiricalRecord['theoreticals'] = pricedRecord_t0.theoreticals
		empiricalRecord['delta'] = {}


		underlyingLastDiff = (underlyingTick_t0.ask - underlyingTick_t1.ask) + (underlyingTick_t0.bid - underlyingTick_t1.bid)
		optionLastDiff = (optionTick_t0.ask - optionTick_t1.ask) + (optionTick_t0.bid - optionTick_t1.bid)

		observedDelta = None
		if underlyingLastDiff == 0 or optionLastDiff == 0:
			observedDelta = np.nan
		else:
			observedDelta = optionLastDiff/underlyingLastDiff

		empiricalRecord['delta']['spread'] = observedDelta


		optionLastDiff = optionTick_t0.last - optionTick_t1.last
		underlyingLastDiff = underlyingTick_t0.last - underlyingTick_t1.last
		observedDelta = None
		if underlyingLastDiff == 0 or optionLastDiff == 0:
			observedDelta = np.nan
		else:
			observedDelta = optionLastDiff/underlyingLastDiff

		empiricalRecord['delta']['last'] = observedDelta


		empiricalData.append(empiricalRecord)
	return empiricalData
