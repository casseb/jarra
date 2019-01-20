from src.common.support import *
from src.service import flow

logging.info(SYSTEM_START_MESSAGE)
@BOT.message_handler(commands=[START_COMMAND])
def listen_start(message):
    flow.receive_start(message)

@BOT.message_handler(content_types=[TEXT_TYPE])
def listen_text(message):
    flow.receive_text(message)

BOT.polling()
