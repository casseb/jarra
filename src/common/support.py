from pymongo import MongoClient
import os
import re
import logging
import telebot
from src.ds.message import Message

#Constants
BOT = telebot.TeleBot(os.environ['BOT_API_TOKEN'])
DB = MongoClient(os.environ['MONGO_URI']).memory

SYSTEM_START_MESSAGE = 'Sistema iniciado'
START_COMMAND = 'start'
HELP_COMMAND = 'help'
TEXT_TYPE = 'text'
SPACE = ' '

MATCH_CREATE_LIST = ['create', 'list', 'lists"1"']
MATCH_ADD_LIST_ITEM = ['add', 'list', 'lists"1"', 'entities"1"']
MATCH_REPEAT = ['repeat', 'entities"1"']

TERMS = ['repeat', 'create', 'list', 'answer', 'add', 'talk']

LIST_WELCOME = '[Bem Vindo] '
LIST_NOT_UNDERSTAND = '[Não Entendi] '
LIST_CREATE_LIST = "[Criado nova lista] "
LIST_ADD_LIST_ITEM = '[Adicionado item na lista] '
LIST_REPEAT = '[Repetindo]: '

REGEX_WORD_IN_COL = r'\[(.+?)\]'
REGEX_WORD_IN_DOUBLE_QUOTES = r'\"(.+?)\"'

DB_LISTS_LIST_NAME = 'list_name'
DB_LISTS_TEXT = 'text'
DB_UNDEFINED_CONTENT = 'content'

HELP_MESSAGE = '## *Bem Vindo ao Smart CasseBot* ##' \
               '\n' \
               '\n' \
               'Ele conversa usando linguagem natural, por isso você não precisa se preocupar tanto em como escreve,' \
               'só seguir sua intuição. Abaixo os comandos já desenvolvidos' \
               '\n' \
               '\n' \
               '## *Definições* ##' \
               '\n' \
               '\n' \
               '-*Listas* são conjuntos de termos que, quando solicitados, retornam um dos itens presentes de forma aleatória, elas são representadas entre [[ ]]' \
               '\n' \
               '*Exemplo:* uma lista chamada [[TEST]] com os itens "teste1", "teste2" e "teste3" pode trazer "teste2" ou "teste3" dependendo da sua sorte' \
               '\n' \
               '\n' \
               '-*Entidades* são termos que representam o que você quer informar ao bot como objetivo, elas são representadas entre " "' \
               '\n' \
               '*Exemplo:* se você quer que o bot repita uma frase, será necessário falar: repita "casa", desta forma o bot sabe exatamente o que ele deve repetir' \
               '\n' \
               '\n' \
               '## *Funcionalidades* ##' \
               '\n' \
               '\n' \
               '-*Criar lista*' \
               '\n' \
               'Cria uma lista, exige exatamente ou os sinônimos das palavras "lista", "criar" e uma lista' \
               '\n' \
               '*Exemplo*: Crie uma lista chamada [[PIADA]]' \
               '\n' \
               '\n' \
               '-*Adicionar item em uma lista*' \
               '\n' \
               'Adiciona um item na lista, exige exatamente ou os sinônimos das palavras "lista", "adicionar", uma entidade e uma lista' \
               '\n' \
               '*Exemplo*: Adicione na lista [[PIADA]] o item "Piu Piu"' \
               '\n' \
               '\n' \
               '-*Repetir*' \
               '\n' \
               'Repete o que foi solicitado pelo usuário, exige exatamente ou os sinônimos das palavras "repetir" e uma entidade' \
               '\n' \
               '*Exemplo*: Repita a frase "A piada do dia é: [[PIADA]]"'



#Log Configuration
level = logging.INFO
format = '%(levelname)s : %(asctime)s : %(message)s'
datefmt = '%d/%m/%Y %I:%M:%S%p'
handlers = [logging.FileHandler('output.log'), logging.StreamHandler()]
logging.basicConfig(level = level, format = format, datefmt = datefmt, handlers = handlers)

def convert_to_Message(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name + SPACE + message.from_user.last_name
    text = message.text
    return Message(user_id, user_name, text)

def list_words_in_col(message):
    return re.findall(REGEX_WORD_IN_COL, message)

def list_word_in_double_quotes(message):
    return re.findall(REGEX_WORD_IN_DOUBLE_QUOTES, message)

def remove_cols(message):
    return message.replace('[','').replace(']','')



