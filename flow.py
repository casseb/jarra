import listen
import understand
import repeat
import talk
import memorize

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
    sense = understand.getSense(message)
    if(sense == 'repeat'):
        talk.audit(user_name + " quer que eu repita o que ele disse!!!")
        repeat.execute(message, user_id, user_name)
    else:
        talk.audit(user_name + " pediu algo que não faço ideia do que seja: " + message)
        talk.byTelegram(user_id, user_name + ', Não entendi nada que você disse!!! "'+ message + '" não faz sentido!!!')
        memorize.createNewUndefinedSense(message)


