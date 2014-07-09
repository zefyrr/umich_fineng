import numpy as np


def computeDeltas(pricedData, positionIndex, useSpread=True):
	(startPositionIndex, endPositionIndex) = positionIndex

	deltas = []
	for i in range(startPositionIndex, endPositionIndex):
		pricedRecord_t0 = pricedData[i]
		pricedRecord_t1 = pricedData[i+1]

		underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
		underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick

		optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
		optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
		

		if useSpread:
			underlyingLastDiff = (underlyingTick_t0.ask - underlyingTick_t1.ask) + (underlyingTick_t0.bid - underlyingTick_t1.bid)
			optionLastDiff = (optionTick_t0.ask - optionTick_t1.ask) + (optionTick_t0.bid - optionTick_t1.bid)
		else:
			optionLastDiff = optionTick_t0.last - optionTick_t1.last
			underlyingLastDiff = underlyingTick_t0.last - underlyingTick_t1.last

		observedDelta = None
		if underlyingLastDiff == 0 or optionLastDiff == 0:
			observedDelta = np.nan
		else:
			observedDelta = optionLastDiff/underlyingLastDiff

		deltas.append((optionTick_t1.timestamp, observedDelta, optionTick_t1.last, underlyingTick_t1.last))
	return deltas
