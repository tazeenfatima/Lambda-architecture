from pymongo import MongoClient, errors
import csv
import datetime
import json

# global variables for MongoDB host (default port is 27017)
DOMAIN = '172.18.0.2'
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    client = MongoClient(
        host = [ str(DOMAIN) + ":" + str(PORT) ],
        serverSelectionTimeoutMS = 3000, # 3 second timeout
        username = "root",
        password = "1234",
    )
    db = client.airline;
    batchData = db.flights.find({'$or':[ 
 {'$and':[{"FL_DATE":{'$gte': '2018-04-01'}},{"FL_DATE": {'$lte':'2018-05-31'}}]},
 {'$and':[{"FL_DATE":{'$gte': '2017-04-01'}},{"FL_DATE": {'$lte':'2017-05-31'}}]}
 ]}, { 'CANCELLED':1, 'ARR_DELAY':1, 'FL_DATE':1, '_id':0 });
    batchStr = str();
    for document in batchData:
      print (document);
      if batchStr:
        batchStr = batchStr + ";";
      batchStr = batchStr + json.dumps(document);
      #batchJson.append(document);
    with open('batch-data1.txt', 'w') as outfile:
      outfile.write(batchStr)

except errors.ServerSelectionTimeoutError as err:
    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)
