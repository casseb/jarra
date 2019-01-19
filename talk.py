import os
import telebot
import memorize
import list_of_answers

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

def audit(message):
    message = "[JARRA]: " + message + "-------------"
    message = list_of_answers.execute(message)
    print(message)
    memorize.saveHistory(message)

def byTelegram(user_id, message):
    bot.send_message(user_id,message)
    memorize.saveHistory("[BOT]: userId " + str(user_id) + " - " + message)

