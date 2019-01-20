import listen
import understand
import repeat
import talk
import memorize
import list_of_answers

match_repeat = ['repeat','entities"1"']
match_create_answer_list = ['create', 'list', 'answer', 'entities"1"']

match_repeat_no_entities = ['repeat']
match_create_answer_list_no_entities = ['create', 'list', 'answer']

def receive_text_message(telegram_message):
    user_id = telegram_message.from_user.id
    user_name = telegram_message.from_user.first_name + " " + telegram_message.from_user.last_name
    message = telegram_message.text
    talk.audit('Recebi ' + message + ' do usuário ' + str(user_id) + ":" + user_name)
    toThink(message, user_id, user_name)

def receive_start_message(telegram_message):
    user_id = telegram_message.from_user.id
    user_name = telegram_message.from_user.first_name + " " + telegram_message.from_user.last_name
    talk.audit('Recebi /start do usuário ' + str(user_id) + ":" + user_name)
    talk.byTelegram(user_id, 'Bem vindo '+user_name)

def toListen(message):
    content = listen.getContent(message)
    toThink(content)
    return listen.rest(content)

def toThink(message, user_id, user_name):
    senses = understand.get_senses(message)

    #fluxo de repetição
    if all(elem in senses for elem in match_repeat):
        repeat.execute(message, user_id)
    #fluxo de adição de uma nova lista
    elif all(elem in senses for elem in match_create_answer_list):
        list_of_answers.create_new_list(user_id, message)

    #fluxo de repetição sem parametros
    elif all(elem in senses for elem in match_repeat_no_entities):
        repeat.execute_no_parameter(message, user_id)
    #fluxo de adição de uma nova lista sem parametros
    elif all(elem in senses for elem in match_create_answer_list_no_entities):
        list_of_answers.create_new_list_no_entities(user_id, message)
    else:
        talk.audit(user_name + " pediu algo que não faço ideia do que seja: " + message)
        talk.byTelegram(user_id, user_name + ', Não entendi nada que você disse!!! "'+ message + '" não faz sentido!!!')
        memorize.createNewUndefinedSense(message)


