import json
import ast

class configuration:
    def __init__(self,inputfile,delimiter,dimentions,measures):
       self.inputfile = inputfile
       self.delimiter = delimiter
       self.dimentions = dimentions
       self.measures = measures


def getdimensions(prow,parray,pseperator):
    rdimension = ""
    for pos in parray:
        rdimension = rdimension + pseperator + prow[pos]
    return rdimension
    
    

with open('config.json') as jconfig:
  j = json.load(jconfig)
  print(j)
  pythonobj = configuration(**j)

  print ("Inputfile :",pythonobj.inputfile)
  print ("Dimentions:",pythonobj.dimentions)
  print ("Measures  :",pythonobj.measures)
# pythonobj.measures = '{3:"sum",4:"sum"}'
# pythonobj.measures = ast.literal_eval(pythonobj.measures)
  print (pythonobj.dimentions['keys'])
  print (pythonobj.measures.values())
  
  results = {}
  fh = open("data.csv","r")
  line = fh.readline()
  lkeys = pythonobj.measures.keys()
  ldimentionkeyspos=[]
  for pos in pythonobj.dimentions['keys'].split(','):
      ldimentionkeyspos.append(int(pos))

  print("lkeys - ",lkeys)
  lnno = 1
  for line in fh.readlines():
      row = line.strip().split(',')
      if lnno % 1000000 == 0:
          print(lnno)
      lnno = lnno + 1
#     ldimensions = row[int(pythonobj.dimentions)]
      ldimensions = getdimensions(row,ldimentionkeyspos,pythonobj.dimentions['seperator'])
      if ldimensions in results.keys():
         lmeasures = results[ldimensions]
         for k in lkeys:
             lmeasures[k] += int(row[int(k)])
      else:
         lmeasures = {}
         for k in lkeys:
             print(k)
             lmeasures[k] = int(row[int(k)])
         print(lmeasures)
      results[ldimensions] = lmeasures
  print(results)
