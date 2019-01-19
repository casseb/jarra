from pymongo import MongoClient
from datetime import datetime
import os

client = MongoClient(os.environ['MONGO_URI'])
db = client.memory

def saveHistory(content):
    history = \
        {
        '_id' : datetime.now(),
        'content' : content
        }
    return db.history.insert_one(history)

def createNewUndefinedSense(content):
    undefinedSense = \
        {
        'content' : content
        }
    return db.undefined_sense.insert(undefinedSense)