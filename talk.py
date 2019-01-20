import os
import telebot
import memorize
import lists
import re

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

def audit(message):
    message = "[Audit]: " + message + "-------------"
    print(message)
    memorize.saveHistory(message)

def byTelegram(user_id, message):
    message = lists.replace_random_item(message)
    bot.send_message(user_id,message)
    memorize.saveHistory("[Bot]: userId " + str(user_id) + " - " + message)

