import remember
import re
import talk
import memorize

def execute(message):
    words = re.findall(r'\[(.+?)\]',message)
    for word in words:
        message = message.replace(word, remember.getRandomAnswer(word))
    message = message.replace('[','').replace(']','')
    return message

def create_new_list(user_id, message):
    entitity = re.findall(r'\"(.+?)\"',message)
    memorize.create_answer_list(entitity[0])
    talk.byTelegram(user_id, "Entendido, salvando esta bodega, criada a lista " + entitity[0])

def create_new_list_no_entities(user_id, message):
    talk.byTelegram(user_id, 'Você não informou qual o nome da lista, '
                                 'repita a frase "' + message +
                                 '" adicionando o nome da lista entre aspas duplas, por obséquio')