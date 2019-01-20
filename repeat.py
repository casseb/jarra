from support import *
import talk

def execute(message):
    entitity = list_word_in_double_quotes(message.text)[0]
    talk.telegram(message.user_id, LIST_REPEAT + entitity)