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

def create_answer_list(content):
    answer_list = \
        {
        'list_name' : content,
        'text' : content
        }
    return db.answers.insert(answer_list)

def add_answer_list_item(list_name, text):
    answer_list = \
        {
            'list_name': list_name,
            'text': text
        }
    return db.answers.insert(answer_list)