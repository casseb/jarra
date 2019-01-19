from pymongo import MongoClient
import os
import random

client = MongoClient(os.environ['MONGO_URI'])
db = client.memory

def getRandomAnswer(list_name):
    answerList = list(db.answers.find({},{"list_name" : list_name}))
    if not answerList:
        return list_name
    else:
        return random.choice(answerList)