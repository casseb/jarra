import nltk
from googletrans import Translator
from nltk.corpus import wordnet as wn

translator = Translator()
terms = ['repeat', 'create', 'list', 'answer']

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
    for term in terms:
        if(compare(wordnet_target, wn.synsets(term))):
            senses.append(term)
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
