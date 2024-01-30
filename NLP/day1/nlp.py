import nltk
from nltk.corpus import webtext


def tokenize(string, method="word"):
    tokens = []
    if method == "word":
        tokens = nltk.tokenize.word_tokenize(string)

    elif method == "sentence":
        tokens = nltk.tokenize.sent_tokenize(string)

    return tokens


def filter_stop_words(string):
    # Tokenize
    tokens = tokenize(string, method="word")

    # Get list of stop words
    stop_words = set(nltk.corpus.stopwords.words("english"))

    filtered_tokens = []

    for word in tokens:
        if word.casefold() not in stop_words:
            filtered_tokens.append(word)

    return filtered_tokens


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


def lemmatize(string):
    # Tokenize
    tokens = tokenize(string, method="word")

    # Init Lemmatizer
    lemmatizer = nltk.stem.WordNetLemmatizer()

    lem_words = [lemmatizer.lemmatize(word) for word in tokens]

    return lem_words


def lemmatize_with_pos(string):
    # get POS
    pos_tags = tag_pos(string, simplify=True)
    # Init lemmatizer
    lemmatizer = nltk.stem.WordNetLemmatizer()
    # POS wrapper
    pos_map = {
        "VERB": "v",
        "ADJ": "a",
        "ADV": "r",
        "NOUN": "n",
    }

    lemmatized_words = []
    for word, pos in pos_tags:
        if pos in pos_map:
            lem_word = lemmatizer.lemmatize(word, pos=pos_map[pos])
        else:
            lem_word = lemmatizer.lemmatize(word)
        lemmatized_words.append(lem_word)

    return lemmatized_words


def chunk(string):
    # GEt POS
    pos_tags = tag_pos(string)
    # Define grammar
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    # Create parser
    parser = nltk.RegexpParser(grammar=grammar)
    # Chunk
    chunk_str = parser.parse(pos_tags)
    return chunk_str


def read_corpus():
    # print(webtext.fileids())
    # print(webtext.readme())
    return webtext.raw('pirates.txt')


if __name__ == "__main__":
    """
    STRING = "Muad'Dib learned rapidly because his first training was in how \
            to learn. And the first lesson of all was the basic trust that he \
            could learn. It's shocking to find how many people do not believe \
            they can learn, and how many more believe learning to be \
            difficult."

    token = tokenize(STRING, method="sentence")
    print(token)
    """

    """
    string = "Sir, I protest. I am not a merry man!"
    filtered_tokens = filter_stop_words(string)
    print(filtered_tokens)
    """

    '''
    string = """
    if you wish to make an apple pie from scratch,
    you must first invent the universe"""

    pos_tags = tag_pos(string, simplify=True)
    print(pos_tags)
    '''

    """ =================== =====================
    string = "The worst thing to do in situations like this is running away"
    lem_words = lemmatize_with_pos(string)
    print(lem_words)
    """

    """
    string = "The quick brown fox jumps over the lazy dog"
    chunk_str = chunk(string)

    print(chunk_str)
    chunk_str.draw()
    """

    read_corpus()
