import sys
import tick_pb2 as proto
import varint 
import csv
import os

dirname = "//Users/sindhuramalireddy/Desktop/project/analysis_20140628/FDX.priced/FDX/FDX/"
dirresult = "/Users/sindhuramalireddy/Desktop/project/analysis_20140628/results/last_traded_socd/"
for filename in os.listdir(dirname):
    fname = dirname + filename + "/option_tick_priced.proto"
    if os.path.exists(fname):
        data = open(fname, "rb").read()             # read file as string
        decoder = varint.decodeVarint32          # get a varint32 decoder
                                                # others are available in varint.py
        next_pos, pos = 0, 0
        data1 = []
        dict={}
        rname = dirresult + filename + ".csv"
        writer = csv.writer(open(rname,'wb'))
        # Loop to read each pricedData object in the file
        while 1:
       	        pricedData = proto.PricedData()
           	try:
          		next_pos, pos = decoder(data, pos)
           	except:
          		break
           	pricedData.ParseFromString(data[pos:pos + next_pos])
            
           	#This is a refersher on how to read the datastructure
            
           	optionBid = pricedData.optionTick.tick.bid
           	optionAsk = pricedData.optionTick.tick.ask
           	optionLast = pricedData.optionTick.tick.last
           	
           	# print underlying
           	stockBid = pricedData.optionTick.underlyingTick.bid
           	stockAsk = pricedData.optionTick.underlyingTick.ask
           	stockLast = pricedData.optionTick.underlyingTick.last
           	
           	# price as the average of bid and ask
           	#optionPrice = optionBid + optionAsk / 2
           	#stockPrice = stockBid + stockAsk / 2
           	
           	# price as the last traded price
           	optionPrice = optionLast
           	stockPrice = stockLast
                data1.append((optionPrice, stockPrice))
                #START calculating empirical delta and comparing it with the set of theoretical deltas
                if len(data1) > 2:
                        #v1 = data1[-1][0]
                        #v0 = data1[-2][0]
                        #s1 = data1[-1][1]
                        #s0 = data1[-2][0]
                        # focd
                        v2 = data1[-1][0]
                        v0 = data1[-3][0]
                        s2 = data1[-1][1]
                        s0 = data1[-3][1]
                        #empDel = (v1 - v0) / (s1 - s0)
                        if (s2-s0) != 0:
                            empDel = (v2 - v0) / (s2 - s0)
                        else:
                            empDel = 10000
                        
                        
                        writer.writerow(['empDelta',empDel])
                        r1 = empDel*0.9
                        r2 = empDel*1.1
                        #print empDel
                        #print "chk", len(dict)
                        #break
                        subDict = {i:j for i,j in dict.iteritems() if r1<j<r2}
                        writer.writerow(['index','theoreticalDelta'])
                        for key, value in subDict.items():
                            writer.writerow([key,value])
                        writer.writerow('\n')
                        #break
                    #END calculating empirical delta and comparing it with the set of theoretical deltas       
           	
           	
           	for theoretical in pricedData.theoreticals:
          		
          		index = theoretical.Id.numDataPoints
          		theoDelta = theoretical.delta
          		dict.update({index:theoDelta})
          		
           	pos += next_pos
       	
        print "done!"
#empDelta=[]
#for i in range(1,len(data1)):
#    diffOption = data1[i-1][0]-data1[i][0]
#    diffStock = data1[i-1][1]-data1[i][1]
#    if diffStock != 0:
#        empDelta.append(diffOption/diffStock)
#    else:
#        empDelta.append(10000)



