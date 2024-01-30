import nltk
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from math import log


def tokenize(string, len=1):
    tokens = nltk.tokenize.word_tokenize(string)
    tags = nltk.pos_tag(tokens)
    tags = [
        (word, nltk.tag.map_tag("en-ptb", "universal", tag))
        for word, tag in tags
    ] 
    words = [tag[0] for tag in tags if tag[1] not in ['.']]
    words = [word.lower() for word in words]
    if len > 1:
        phrases = []
        for index, word in enumerate(words):
            phrases.append(tuple(words[index:index+len]))
        return phrases
    return words

def get_unique_words(documents, search_len):
    unique_words = []
    for doc in documents:
        tokens = tokenize(doc, search_len)
        unique_words.extend(tokens)

    return set(unique_words)

def get_tf(tokens, unique_words):
    length = len(tokens)
    freq_dist = (dict(nltk.FreqDist(tokens)))

    words_present = [word for word in unique_words if (word in tokens)]

    words_absent = [word for word in unique_words if word not in tokens]

    tf = {}

    for word in words_present:
        tf[word] = freq_dist[word]/length
    
    for word in words_absent:
        tf[word] = 0

    return tf


def get_idf(unique_words, tf, smoothing):
    num_of_docs = (len(tf.keys()))
    if smoothing:
        num_of_docs +=1

    idf={}
    for word in unique_words:
        present = 1 if smoothing else 0
        for doc in tf:
            if (tf[doc][word] != 0):
                present += 1
        idf[word] = log(num_of_docs/present)
    
    return (idf)


def get_tfidf(document, documents, search_len,is_isd_smoothed=False):

    token_main = tokenize(str(document), search_len)

    unique_words = get_unique_words(documents, search_len)
    
    main = 'doc_main_tf'
    tfs = {}
    for index, doc in enumerate(documents):
        
        tokens = tokenize(doc, search_len)
        key_name = f'doc{index}_tf' if tokens != token_main else main

        tfs[key_name] = get_tf(tokens, unique_words)

    idfs = get_idf(unique_words,tfs, is_isd_smoothed)

    tf_idf = {}
    for word in tfs[main]:
        tf_idf[word] = (tfs[main][word]) * idfs[word]

    sorted_tfidf = sorted(tf_idf.items(), key=lambda x:x[1])
    sorted_tfidf = dict(sorted_tfidf)

    return (sorted_tfidf)


    
def listTopSearchResuilts(search_string, documents):

    search_result = {}

    tokens = tokenize(search_string)
    search_length = len(tokens)
    
    for document in documents:
        tf_idf = (get_tfidf(documents[document], documents.values(), search_length))
        # tf_keys = ([" ".join(x) for x in list(tf_idf.keys())]) if search_length > 1 else list(tf_idf.keys())
        tf_keys = list(tf_idf.keys())
        if not (tuple(tokens) in tf_keys):
            continue
        search = tuple(tokens) if search_length > 1 else search_string
        search_result[document] = tf_idf[search]

    sorted_tfidf = sorted(search_result.items(), key=lambda x:x[1], reverse=True)
    sorted_tfidf = dict(sorted_tfidf)

    print(list(sorted_tfidf.items())[0:9])
        

if __name__ == "__main__":
    documents = {}
    path = 'songs'

    for title in os.listdir(path):
        file = os.path.join(path, title)
        try:
            with open(file, 'r') as f:
                documents[title] = (f.read())

        except FileNotFoundError as e:
            print(f)
            print("file not found")

    # documents = {
    # "1":"Ang bango bango, ang bango bango ang bango bango ng bulaklak",
    # "2":"Bahay kubo kahit munti ang halaman doon ay sari-sari",
    # "3":"Ang bahay ko ay may bulaklak pero hindi masyadong mabango"
    # }
    

    search_string = input("Please enter word to search: ")
    listTopSearchResuilts(search_string, documents)