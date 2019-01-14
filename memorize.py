from pymongo import MongoClient
from datetime import datetime
import talk

client = MongoClient('localhost', 27017)
db = client.memory

def saveHistory(content):
    talk.byLog("Vou tentar memorizar")
    history = {'datetime' : datetime.now(), 'content' : content}
    talk.byLog("Acho que consegui hehehehehe")
    return db.history.insert_one(history)