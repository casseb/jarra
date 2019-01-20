from src.common.support import *
from src.service import talk
from src.repository import memorize, remember


def replace_random_item(message):
    words = list_words_in_col(message)
    for word in words:
        message = message.replace(word, remember.random_item(word))
    message = remove_cols(message)
    return message

def create_new_list(message):
    list_name = list_words_in_col(message.text)[0]
    memorize.create_list(list_name)
    talk.telegram(message.user_id, LIST_CREATE_LIST + list_name)

def add_new_item(message):
    item = list_word_in_double_quotes(message.text)[0]
    list_name = list_words_in_col(message.text)[0]
    memorize.add_answer_list_item(list_name, item)
    talk.telegram(message.user_id, LIST_ADD_LIST_ITEM + item + "->" + list_name)