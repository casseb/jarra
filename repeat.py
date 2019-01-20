import talk
import re

def execute(message, user_id):
    entitity = re.findall(r'\"(.+?)\"', message)[0]
    talk.byTelegram(user_id, '[Repetindo]: '+entitity)