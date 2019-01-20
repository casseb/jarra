from pymongo import MongoClient
import os
import random

client = MongoClient(os.environ['MONGO_URI'])
db = client.memory

def getRandomAnswer(list_name):
    answer_record_list = list(db.answers.find({"list_name" : list_name}))
    if not answer_record_list:
        return list_name
    else:
        answer_list = []
        for answer in answer_record_list:
            answer_list.append(answer.get('text'))
        return random.choice(answer_list)