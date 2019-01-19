import os
import telebot
import flow
import talk

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

talk.audit("[Estou pronto!]")

@bot.message_handler(commands=['start'])
def listen_start(message):
    flow.receive_start_message(message)

@bot.message_handler(content_types=['text'])
def listen_telegram_text(message):
    flow.receive_text_message(message)

bot.polling()
