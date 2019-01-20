import remember
import re
import talk
import memorize

def replace_random_item(message):
    words = re.findall(r'\[(.+?)\]',message)
    for word in words:
        message = message.replace(word, remember.getRandomAnswer(word))
    message = message.replace('[','').replace(']','')
    return message

def create_new_list(user_id, message):
    list = re.findall(r'\[(.+?)\]',message)[0]
    memorize.create_answer_list(list)
    talk.byTelegram(user_id, "[Criado nova lista] " + list)

def add_new_item(user_id, message):
    item = re.findall(r'\"(.+?)\"',message)[0]
    list_name = re.findall(r'\[(.+?)\]',message)[0]
    memorize.add_answer_list_item(list_name, item)
    talk.byTelegram(user_id, '[Adicionado item na lista] ' + item + "->" + list_name)