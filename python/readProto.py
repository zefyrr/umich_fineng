import tick_pb2 as proto
import varint


def getInstrumentIterator(input):
	inputFh = open(input, "rb")
	data  = inputFh.read()
	decoder = varint.decodeVarint32
	next_pos, pos = 0, 0
	# Loop to read each pricedData object in the file

	pricedData = []
	lastOptionMeta = None
	while 1:
		pricedRecord = proto.PricedRecord()

		try:
			next_pos, pos = decoder(data, pos)
		except:
			break
		pricedRecord.ParseFromString(data[pos:pos + next_pos])
		pos += next_pos

		optionMeta = pricedRecord.pairedTick.optionMeta
		if lastOptionMeta:
			if lastOptionMeta.instrument !=  optionMeta.instrument:
				yield (lastOptionMeta, pricedData)
				pricedData = []

		pricedData.append(pricedRecord)
		lastOptionMeta = optionMeta

	inputFh.close()
	yield (lastOptionMeta, pricedData)