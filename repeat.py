import talk
import re

def execute(message, user_id):
    entitity = re.findall(r'\"(.+?)\"', message)[0]
    talk.byTelegram(user_id, 'Então você quer que eu repita: "'+entitity+'" ????')

def execute_no_parameter(message, user_id):
    talk.byTelegram(user_id, 'Você não informou o que devo repetir, '
                             'repita a frase "' + message +
                    '" adicionando o que devo repetir entre aspas duplas, por obséquio')