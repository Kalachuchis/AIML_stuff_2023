import nltk
import numpy as np
import re

from nltk.corpus import webtext


def tokenizer_words_only(string, method='word'):
    # tokenizer = nltk.tokenize.RegexpTokenizer('<\/?\w+>|\w+-\w+|\w+')
    tokenizer = nltk.tokenize.RegexpTokenizer('\s', gaps=True)
    tokens = tokenizer.tokenize(string)
    stop_words = set(nltk.corpus.stopwords.words("english"))

    filtered_tokens = []

    for word in tokens:
        if word.casefold() not in stop_words:
            filtered_tokens.append(word)

    return filtered_tokens


def tokenize(string, method="word"):
    tokens = []
    if method == "word":
        tokens = nltk.tokenize.word_tokenize(string)

    elif method == "sentence":
        tokens = nltk.tokenize.sent_tokenize(string)

    return tokens


def tag_pos(string, simplify=False):
    # Tokenize
    tokens = tokenize(string, method="word")

    # Tag POS
    tags = nltk.pos_tag(tokens)  # nltk.help.upenn_tagset("WRB")

    # Simpify if specified
    if simplify:
        tags = [
            (word, nltk.tag.map_tag("en-ptb", "universal", tag))
            for word, tag in tags
        ]
    return tags


def create_vocab(n=3):
    wine_txt = (webtext.raw('wine.txt'))
    tokens = tag_pos(wine_txt, simplify=True)

    # removing HTML tags
    # pattern = '^(<\/?\w+>|\/\w+)?'
    pattern = '^\W+?'
    words = [word[0] for word in tokens if not re.match(pattern, word[0])]

    file = f'{n}gram_vocab.txt'
    with open(file, 'w', encoding='utf-8') as f:
        for index in range(len(words)-n + 1):
            # print(word)
            f.write(str(" ".join(words[index:index+n])))
            f.write('\n')

    f.close()


def vectorize_bag_of_words(string, n=3):
    file = f'{n}gram_vocab.txt'
    try:
        with open(file, 'r', encoding='utf-8') as f:
            vocab_list = f.read().split('\n')
    except FileNotFoundError as e:
        print("No file found. Creating a file please wait...")
        create_vocab(n)
        with open(file, 'r', encoding='utf-8') as f:
            vocab_list = f.read().split('\n')
    except Exception as e:
        print(e)

    tokens = tokenize(string)
    phrases = []
    for index in range(len(tokens)-n + 1):
        phrase = (" ".join(tokens[index:index+n]))
        phrases.append(phrase.lower())

    vectored = [phrases.count(vocab.lower()) for vocab in vocab_list]
    print(np.array(vectored))


if __name__ == "__main__":
    string = "Lovely delicate fragrant delicate fragrant Rhone"
    vectorize_bag_of_words(string)
