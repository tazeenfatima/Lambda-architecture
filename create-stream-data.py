from pymongo import MongoClient, errors

# global variables for MongoDB host (default port is 27017)
DOMAIN = '172.18.0.3'
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
    batchData = db.flights.find({'$and':[{"FL_DATE":{'$gte': '2018-11-01'}},{"CANCELLED": {'$eq':'0.0'}},
{"FL_DATE": {'$lte':'2018-11-30'}} ]},
{'ARR_DELAY':1, 'FL_DATE':1, '_id':0 });
    batchStr = str();
    for document in batchData:
      print (document);
      batchStr = batchStr + "XADD streams * FL_DATE " + document["FL_DATE"] + " ARR_DELAY " + document["ARR_DELAY"] + "\n";
      #batchJson.append(document);
    with open('stream-data2.txt', 'w') as outfile:
      outfile.write(batchStr)

except errors.ServerSelectionTimeoutError as err:
    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)
