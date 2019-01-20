from src.common.support import *
import random

def random_item(list_name):
    record_list = list(DB.lists.find({DB_LISTS_LIST_NAME : list_name}))
    if not record_list:
        return list_name
    else:
        answer_list = []
        for answer in record_list:
            answer_list.append(answer.get(DB_LISTS_TEXT))
        return random.choice(answer_list)

def is_list_name_set(list_name):
    if list(DB.lists.find({DB_LISTS_LIST_NAME : list_name})):
        return True
    return False