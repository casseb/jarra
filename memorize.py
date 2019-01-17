from pymongo import MongoClient
from datetime import datetime
import talk
import os

client = MongoClient(os.environ['MONGO_URI'])
db = client.memory

def saveHistory(content):
    talk.byLog("Vou tentar memorizar")
    history = {'datetime' : datetime.now(), 'content' : content}
    talk.byLog("Acho que consegui hehehehehe")
    return db.history.insert_one(history)