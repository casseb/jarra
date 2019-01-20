from src.common.support import *

def createNewUndefinedSense(content):
    undefinedSense = \
        {
        DB_UNDEFINED_CONTENT : content
        }
    return DB.undefined_sense.insert(undefinedSense)

def create_list(content):
    answer_list = \
        {
        DB_LISTS_LIST_NAME : content,
        DB_LISTS_TEXT : content
        }
    return DB.lists.insert(answer_list)

def add_answer_list_item(list_name, text):
    answer_list = \
        {
        DB_LISTS_LIST_NAME : list_name,
        DB_LISTS_TEXT : text
        }
    return DB.lists.insert(answer_list)