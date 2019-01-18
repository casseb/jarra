from pymongo import MongoClient
from datetime import datetime
import talk
import os

client = MongoClient(os.environ['MONGO_URI'])
db = client.memory

def saveHistory(content):
    history = {'datetime' : datetime.now(), 'content' : content}
    return db.history.insert_one(history)