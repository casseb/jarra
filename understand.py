import nltk
from googletrans import Translator
from nltk.corpus import wordnet as wn

translator = Translator()
wordnetRepeat = wn.synsets('repeat')

def getSense(message):
    englishMessage = translator.translate(message).text
    tokens = nltk.word_tokenize(englishMessage)

    if(isRepeat(tokens)):
        return 'repeat'
    else:
        return 'none'

def isRepeat(tokens):
    for token in tokens:
        wordnetToken = wn.synsets(token)
        if(len(wordnetToken) == 0):
            continue
        similarity = wordnetRepeat[0].path_similarity(wordnetToken[0])
        if(similarity > 0.8):
            return True
    return False