from src.common.support import *
from src.service import lists, repeat, talk, understand
from src.repository import memorize


def receive_start(message):
    message = convert_to_Message(message)
    logging.info(str(message))
    talk.telegram(message.user_id, LIST_WELCOME + message.user_name)

def receive_help(message):
    message = convert_to_Message(message)
    logging.info(str(message))
    talk.telegram_help(message.user_id, HELP_MESSAGE)

def receive_text(message):
    message = convert_to_Message(message)
    logging.info(str(message))
    to_think(message)

def to_think(message):
    senses = understand.get_senses(message.text)
    if all(elem in senses for elem in MATCH_CREATE_LIST):
        lists.create_new_list(message)
    elif all(elem in senses for elem in MATCH_ADD_LIST_ITEM):
        lists.add_new_item(message)
    elif all(elem in senses for elem in MATCH_REPEAT):
        repeat.execute(message)
    else:
        talk.telegram(message.user_id, LIST_NOT_UNDERSTAND + message.text)
        memorize.createNewUndefinedSense(message.text)