import re
from xml.etree import ElementTree

import nltk
from nltk.collocations import *

def find_collocations (tokens_list):

    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(tokens_list)
    finder.apply_freq_filter(10)
    print(finder.nbest(bigram_measures.pmi, 15))


def make_a_freq_list (tokens_list):

    tokens_freq = {}
    for i in tokens_list:
        if (i in tokens_freq.keys()):
            tokens_freq[i] += 1
        else:
            tokens_freq[i] = 1

    #dict to list
    tokens_freq_list = []
    for i in tokens_freq:
        tokens_freq_list.append([i, tokens_freq[i]])

    tokens_freq_list.sort(key = lambda x:x[1], reverse = True)
    print (tokens_freq_list[:15])


def get_clean_data_from_flextext (corpus_file):
    clean_txt = ""
    tree = ElementTree.parse(corpus_file)
    root = tree.getroot()

    for phrase in root.findall("./interlinear-text/paragraphs/paragraph/phrases/phrase"):
        sentence = phrase.find('item').text

        clean_sentence = ""
        for word in phrase.findall("words/word/item[@type='txt']"):
            word_txt = word.text
            clean_sentence = clean_sentence + word_txt + " "

        clean_sentence = clean_sentence.strip() #remove the last space
        clean_txt = clean_txt + clean_sentence + "\n"

    clean_txt = clean_txt.strip() #remove the last \n
    
    return clean_txt


def main ():

    corpus_file = "lab4_corpus.flextext"
    clean_txt = get_clean_data_from_flextext (corpus_file)
    tokens_list = clean_txt.split()


    find_collocations (tokens_list)
    make_a_freq_list (tokens_list)



if __name__ == '__main__':
    main ()
