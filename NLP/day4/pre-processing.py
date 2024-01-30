import os
import re
from typing import List

import nltk
import numpy as np
import pandas as pd
from nltk.tokenize import RegexpTokenizer


def tokenize(string, method="word"):

    tokenizer = RegexpTokenizer(
        "(?:(?<=\s)|(?<=^)|(?<=[>\”]))[a-z-’]+(?:(?=\s)|(?=\:\s)|(?=$)|(?=[.!,;\”]))"
    )
    # tokens = nltk.tokenize.word_tokenize(string.lower())
    tokens = tokenizer.tokenize(string.lower())
    tags = nltk.pos_tag(tokens)
    tags = [
        (word, nltk.tag.map_tag("en-ptb", "universal", tag))
        for word, tag in tags
    ]
    words = [tag[0] for tag in tags if tag[1] not in ["."]]

    return words


def generate_vocabulary(documents):
    tokens = []
    for doc in documents:
        tokens.extend(tokenize(doc))
    fdist = nltk.FreqDist(tokens)
    unique_words = list((dict(fdist).keys()))

    vocabulary = "\n".join(unique_words)

    with open("training_vocab.txt", "w", encoding="utf-8") as f:
        f.write(vocabulary)

    f.close()


def generate_dcount_vectors(vocabulary, documents) -> pd.DataFrame:
    df = pd.DataFrame(vocabulary, columns=["Vocabulary"])
    spam_rows = []
    for index, doc in enumerate(documents["spam"]):
        tokens = tokenize(doc)
        spam_data = [["spam", index, doc, token] for token in tokens]
        spam_rows.extend(spam_data)

    ham_rows = []
    for index, doc in enumerate(documents["ham"]):
        tokens = tokenize(doc)
        ham_data = [["ham", index, doc, token] for token in tokens]
        ham_rows.extend(ham_data)

    df_spam = pd.DataFrame(
        spam_rows, columns=["Doc_Class", "Doc_Id", "Message", "Vocabulary"]
    )
    vector_df_spam = df_spam.pivot_table(
        index="Doc_Id", columns="Vocabulary", aggfunc="size", fill_value=0
    )
    df_spam = pd.merge(df_spam, vector_df_spam, on="Doc_Id", how="right")

    df_ham = pd.DataFrame(
        ham_rows, columns=["Doc_Class", "Doc_Id", "Message", "Vocabulary"]
    )
    vector_df_ham = df_ham.pivot_table(
        index="Doc_Id", columns="Vocabulary", aggfunc="size", fill_value=0
    )
    df_ham = pd.merge(df_ham, vector_df_ham, on="Doc_Id", how="right")


    vectored_df = pd.concat([df_ham, df_spam], ignore_index=True)

    # df_copy = df.set_index('Vocabulary')
    # print(df_copy.to_json())
    vectored_df = vectored_df.fillna(0)
    vectored_df = vectored_df.drop(columns=["Vocabulary"])
    vectored_df = vectored_df.drop_duplicates(ignore_index=True)

    return vectored_df


def reduce_vocabulary(vocabulary: List, dcount_vectors: pd.DataFrame, size):
    ham_df = dcount_vectors.loc[dcount_vectors["Doc_Class"] == "ham"]
    spam_df = dcount_vectors.loc[dcount_vectors["Doc_Class"] == "spam"]
    num_of_spams = len(spam_df)
    num_of_hams = len(ham_df)
    reduced = []
    for word in vocabulary:
        num_of_docs_with_word_ham = (ham_df[word] != 0).sum()
        num_of_docs_with_word_spam = (spam_df[word] != 0).sum()

        if num_of_docs_with_word_ham == 0 or num_of_docs_with_word_spam == 0:
            num_of_docs_with_word_spam += 1
            num_of_docs_with_word_ham += 1

        prob_spam = num_of_docs_with_word_spam / num_of_spams
        prob_ham = num_of_docs_with_word_ham / num_of_hams

        spammicity = prob_spam / prob_ham
        hammicity = prob_ham / prob_spam
        doc_class = "spam" if spammicity > hammicity else "ham"
        polarity = spammicity if spammicity > hammicity else hammicity
        row = [
            doc_class,
            word,
            num_of_docs_with_word_ham,
            num_of_docs_with_word_spam,
            polarity,
        ]
        reduced.append(row)

    polarity_df = pd.DataFrame(
        reduced,
        columns=[
            "doc_class",
            "vocabulary",
            "ham_count",
            "spam_count",
            "polarity",
        ],
    )

    polarity_spam = polarity_df.loc[polarity_df["doc_class"] == "spam"]
    polarity_ham = polarity_df.loc[polarity_df["doc_class"] == "ham"]

    spam_reduced = (
        polarity_spam.sort_values(by="polarity", ascending=False)
    ).head(size)
    spam_reduced = spam_reduced.set_index("vocabulary")
    ham_reduced = (
        polarity_ham.sort_values(by="polarity", ascending=False)
    ).head(size)
    ham_reduced = ham_reduced.set_index("vocabulary")

    spam_file = open(f"spam_polarity_{size}.json", "w", encoding="utf-8")
    ham_file = open(f"ham_polarity_{size}.json", "w", encoding="utf-8")

    spam_file.write(spam_reduced.to_json(orient="index"))
    ham_file.write(ham_reduced.to_json(orient="index"))


if __name__ == "__main__":
    documents = {}
    spam = []
    ham = []
    path = "emails"

    pattern = "spam"
    for title in os.listdir(path):
        file = os.path.join(path, title)
        try:
            with open(file, "r", encoding="utf-8") as f:
                # documents[title] = (f.read())

                if re.search(pattern, title):
                    spam.append(f.read())
                else:
                    ham.append(f.read())

            f.close()
        except FileNotFoundError as e:
            print(e)
            print("file not found")

    documents["spam"] = spam
    documents["ham"] = ham
    all_docs = np.array(list(documents.values()))
    all_docs = all_docs.flatten()

    try:
        with open("training_vocab.txt", "r", encoding="utf-8") as f:
            vocab = f.read().split("\n")
        f.close()
    except FileNotFoundError:
        print("Vocabulary not found. Creating vocabulary, please wait...")
        generate_vocabulary(all_docs)
        with open("training_vocab.txt", "r", encoding="utf-8") as f:
            vocab = f.read().split("\n")
        f.close()

    dcount_vectors = generate_dcount_vectors(vocab, documents)

    reduce_vocabulary(vocab, dcount_vectors, 100)
