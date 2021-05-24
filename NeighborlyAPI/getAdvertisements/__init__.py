import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://myazurecosmosdbase:WqBp95cs2bMuUGtJhSSYGRGN6UdZGzCRhCrN0KqPQhL74i0kJrxUIDMGCh4z0RbbT2mRoGTLo3jClkW3ORN8Vw==@myazurecosmosdbase.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@myazurecosmosdbase@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['myazurecosmosdbase']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

