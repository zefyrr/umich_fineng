import time


def getTimeGMTFromUTCEpoch(epochs):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epochs/1000))


def getTimeInSecs(timeStr):
	time = map(lambda x: int(x),  timeStr.split(':'))
	timeSecs = (time[0] * 24 * 60) + (time[1] * 60) + time[2]
	return timeSecs

def getInstrumentMetaStr(optionMeta):
	return '%s %f %s' % (optionMeta.instrument, optionMeta.strike, getTimeGMTFromUTCEpoch(optionMeta.expirationDate))