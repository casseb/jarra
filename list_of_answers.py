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
    entitity = re.findall(r'\"(.+?)\"',message)[0]
    memorize.create_answer_list(entitity)
    talk.byTelegram(user_id, "Entendido, salvando esta bodega, criada a lista " + entitity)

def create_new_list_no_entities(user_id, message):
    talk.byTelegram(user_id, 'Você não informou qual o nome da lista, '
                                 'repita a frase "' + message +
                                 '" adicionando o nome da lista entre aspas duplas, por obséquio')

def add_new_item_no_entities(user_id, message):
    talk.byTelegram(user_id, 'Você não informou qual o nome da lista nem o item que deseja adicionar, '
                                 'repita a frase "' + message +
                                 '" adicionando o nome da lista e item entre aspas duplas, por obséquio')

def add_new_item_one_entities(user_id, message):
    talk.byTelegram(user_id, 'Você não informou qual o nome da lista ou o item que deseja adicionar, '
                                 'repita a frase "' + message +
                                 '" adicionando o nome da lista ou o item entre aspas duplas, por obséquio')

def add_new_item(user_id, message):
    entities = re.findall(r'\"(.+?)\"',message)
    list_name = None
    item = None
    for entity in entities:
        if remember.is_list_name_set(entity):
            list_name = entity
        else:
            item = entity
    if not list_name:
        talk.byTelegram(user_id, 'A lista de respostas informadas ainda não existe, '
                                 'peço que crie primeiro para depois adicionar itens.'
                                 'Exemplo: "Crie uma lista de respotas chamada "' + entities[0] + '"')
    elif not item:
        talk.byTelegram(user_id, 'Os dois itens que você enviou são listas de respostas,'
                                 'deixar cria-los causaria altas tretas!!!!')
    else:
        memorize.add_answer_list_item(list_name, item)
        talk.byTelegram(user_id, 'Excelente, adicionei '+ item + " para a lista " + list_name + ".")