import tick_pb2 as proto
import varint



def getInstrumentIterator(pricedFile, instrumentFilter=None):

	# Loop to read each pricedData object in the file

	pricedData = []
	lastOptionMeta = None

	for pricedRecord in readProto(pricedFile):
		optionMeta = pricedRecord.pairedTick.optionMeta

		if lastOptionMeta:
			if lastOptionMeta.instrument !=  optionMeta.instrument:
				if len(pricedData) > 0:
					yield (lastOptionMeta, pricedData)
				pricedData = []

		lastOptionMeta = optionMeta

		if instrumentFilter and optionMeta.instrument not in instrumentFilter:
			continue


		pricedData.append(pricedRecord)

	if len(pricedData) > 0:
		yield (lastOptionMeta, pricedData)


def readProto(pricedFile):
	inputFh = open(pricedFile, "rb")
	data  = inputFh.read()
	decoder = varint.decodeVarint32
	next_pos, pos = 0, 0
	while 1:
		pricedRecord = proto.PricedRecord()

		try:
			next_pos, pos = decoder(data, pos)
		except:
			break
		pricedRecord.ParseFromString(data[pos:pos + next_pos])
		yield pricedRecord
		pos += next_pos
	inputFh.close()
