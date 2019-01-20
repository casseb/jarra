from src.common.support import *
from src.service import lists


def telegram(user_id, message):
    message = lists.replace_random_item(message)
    BOT.send_message(user_id, message)
    logging.info(str(user_id) + "--->" + message)