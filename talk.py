import os
import telebot

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

def byLog(message):
    print("[JARRA]: ",message,"-------------")

def byTelegram(user_id, message):
    bot.send_message(user_id,message)

def missingSense():
    byLog('Vixi, não entendi nada')

