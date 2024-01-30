import nltk
import numpy as np

from nltk.corpus import webtext


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


def create_vocab():
    wine_txt = (webtext.raw('wine.txt'))
    tokens = tag_pos(wine_txt, simplify=True)
    words_tag = [token for token in tokens if(token[1] not in ['.'])]

    words = [word[0] for word in words_tag if(word[0] not in ['*'])]
    fdist = nltk.FreqDist(words)
    unique_words = list((dict(fdist).keys()))

    with open('vocab.txt', 'w', encoding='utf-8') as f:
        for word in unique_words:
            # print(word)
            f.write(word)
            f.write('\n')

    f.close()


def vectorize_bag_of_words(string):
    try:
        with open('vocab.txt', 'r', encoding='utf-8') as f:
            vocab_list = tokenize(f.read())
    except FileNotFoundError as e:
        create_vocab()
        with open('vocab.txt', 'r', encoding='utf-8') as f:
            vocab_list = tokenize(f.read())
    except Exception as e:
        print(e)

    tokens = tokenize(string)
    tokens = [token.lower() for token in tokens]

    vectored = [tokens.count(vocab.lower()) for vocab in vocab_list]

    return np.array(vectored)


def vectorize_bag_of_words(string, n=3):
    try:
        with open('vocab.txt', 'r', encoding='utf-8') as f:
            vocab_list = tokenize(f.read())
    except FileNotFoundError as e:
        create_vocab(n)
        with open('vocab.txt', 'r', encoding='utf-8') as f:
            vocab_list = tokenize(f.read())
    except Exception as e:
        print(e)

    tokens = tokenize(string)
    tokens = [token.lower() for token in tokens]

    vectored = [tokens.count(vocab.lower()) for vocab in vocab_list]

    return np.array(vectored)


if __name__ == "__main__":
    # create_vocab()
    string = "lovely lovely wine wine"
    print(vectorize_bag_of_words(string))
