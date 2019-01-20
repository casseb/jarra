from src.common.support import *
import nltk
from googletrans import Translator
from nltk.corpus import wordnet as wn

translator = Translator()

def get_senses(message):
    englishMessage = translator.translate(message).text
    tokens = nltk.word_tokenize(englishMessage)
    wordnet_target = []
    senses = []
    for token in tokens:
        wordnet_targets = wn.synsets(token)
        if not wordnet_targets:
            continue
        wordnet_target.append(wordnet_targets)
    for term in TERMS:
        if(compare(wordnet_target, wn.synsets(term))):
            senses.append(term)
    senses = locate_entities(senses, message)
    senses = locate_answer_list(senses, message)
    return senses

def compare(wordnet_targets_list, wordnet_origins):
    for wordnet_targets in wordnet_targets_list:
        for wordnet_target in wordnet_targets:
            for wordnet_origin in wordnet_origins:
                similarity = wordnet_target.path_similarity(wordnet_origin)
                if not similarity:
                    continue
                if(similarity > 0.8):
                    return True
    return False

def locate_entities(senses, message):
    entities = list_word_in_double_quotes(message)
    if not entities:
        return senses
    senses.append('entities"'+ str(len(entities)) +'"')
    return senses

def locate_answer_list(senses, message):
    entities = list_words_in_col(message)
    if not entities:
        return senses
    senses.append('lists"' + str(len(entities)) + '"')
    return senses