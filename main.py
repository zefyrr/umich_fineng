import sys
import os
import tick_pb2 as proto
import varint 
import csv
import numpy as np

def main():
    dirpath = "//Users/sindhuramalireddy/Desktop/project/analysis_20140628/FDX.priced/FDX/FDX/"
    for filename in os.listdir(dirpath):
        fname = dirpath + filename + "/option_tick_priced.proto"
        print fname
        if os.path.exists(fname):
            file = open(fname, "rb")
            data = file.read()                 # read file as string
            decoder = varint.decodeVarint32          # get a varint32 decoder
                                               
            next_pos, pos = 0, 0
            
            lastRecord = []
            currentRecord = []
            writer = csv.writer(open("test_main.csv",'wb'))
            while 1:
       	        currentRecord = proto.PricedData()
       	        
           	try:
          		next_pos, pos = decoder(data, pos)
           	except:
          		break
           	currentRecord.ParseFromString(data[pos:pos + next_pos])
           	pos += next_pos
           	
       	        
           	currentOptionMeta = currentRecord.optionTick.optionMeta
           	
           	
		if lastRecord:
		      lastOptionMeta = lastRecord.optionTick.optionMeta
		      if lastOptionMeta.instrument ==  currentOptionMeta.instrument:
			    s0 = lastRecord.optionTick.underlyingTick.last
			    s1 = currentRecord.optionTick.underlyingTick.last
			    v0 = lastRecord.optionTick.tick.last
			    v1 = currentRecord.optionTick.tick.last
			    if (s0-s1) != 0:
			         empDelta = (v0-v1)/(s0-s1)
			    else:
			         empDelta = np.nan
			    dict={}    
		            for theoretical in lastRecord.theoreticals:
          		        index = theoretical.Id.numDataPoints
                  		theoDelta = theoretical.delta
                  		dict.update({index:theoDelta})
                  		
                  	    r1 = empDelta*0.9
                            r2 = empDelta*1.1
                            
                            writer.writerow(['Instrument',lastOptionMeta.instrument, 'EmpDelta', empDelta])
                            subDict = {i:j for i,j in dict.iteritems() if r1<j<r2}
                            writer.writerow(['index','theoreticalDelta'])
                            for key, value in subDict.items():
                                writer.writerow([key,value])
                            writer.writerow('\n')
	        
                lastRecord = currentRecord
            print "done!"
            break
            file.close()
            
if __name__ == "__main__":
    main()	    
			 