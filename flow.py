import listen
import understand
import repeat
import talk

def receive_text_message(telegram_message):
    user_id = telegram_message.from_user.id
    user_name = telegram_message.from_user.first_name + " " + telegram_message.from_user.last_name

def receive_start_message(telegram_message):
    user_id = telegram_message.from_user.id
    user_name = telegram_message.from_user.first_name + " " + telegram_message.from_user.last_name
    talk.byLog('Recebi /start do usuário '+ str(user_id) + ":" + user_name)
    talk.byTelegram(user_id, 'Bem vindo '+user_name)

def toListen(message):
    content = listen.getContent(message)
    toThink(content)
    return listen.rest(content)

def toThink(message):
    sense = understand.getSense(message)
    if(sense == 'repeat'):
        repeat.execute(message)
    else:
        talk.missingSense()


