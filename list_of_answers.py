import remember
import re

def execute(message):
    words = re.split(r'[ ](?=[*])', message)
    for word in words:
        pure_word = word.replace('[','').replace(']','')
        message = message.replace(word, remember.getRandomAnswer(pure_word))
    return message