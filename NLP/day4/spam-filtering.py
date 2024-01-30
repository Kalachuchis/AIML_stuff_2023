import math
import os
import re

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
    # df_spam = df_spam.groupby('Vocabulary').size().reset_index(name='Count_Spam')
    # vector_df_spam = pd.get_dummies(df_spam['Vocabulary'])
    vector_df_spam = df_spam.pivot_table(
        index="Doc_Id", columns="Vocabulary", aggfunc="size", fill_value=0
    )
    df_spam = pd.merge(df_spam, vector_df_spam, on="Doc_Id", how="right")

    df_ham = pd.DataFrame(
        ham_rows, columns=["Doc_Class", "Doc_Id", "Message", "Vocabulary"]
    )
    # df_ham = df_ham.groupby('Vocabulary').size().reset_index(name='Count_Ham')
    vector_df_ham = df_ham.pivot_table(
        index="Doc_Id", columns="Vocabulary", aggfunc="size", fill_value=0
    )
    # vector_df_ham= pd.get_dummies(df_ham['Vocabulary'])
    df_ham = pd.merge(df_ham, vector_df_ham, on="Doc_Id", how="right")

    # df = df.merge(df_spam, on='Vocabulary', how='left').merge(df_ham, on='Vocabulary', how='left')

    vectored_df = pd.concat([df_ham, df_spam], ignore_index=True)

    # df_copy = df.set_index('Vocabulary')
    # print(df_copy.to_json())
    vectored_df = vectored_df.fillna(0)
    vectored_df = vectored_df.drop(columns=["Vocabulary"])
    vectored_df = vectored_df.drop_duplicates(ignore_index=True)

    return vectored_df


def generate_binary_vector(document, vocabulary):
    tokens = tokenize(document)
    vocab_array = np.array(vocabulary)
    binary_vector = np.isin(vocab_array, tokens)
    binary_vector = binary_vector.astype(int)
    vector_with_vocab = np.vstack([vocab_array, binary_vector])

    # vector_df = pd.DataFrame([binary_vector], columns=vocab_array)
    return vector_with_vocab


def classify_spam_ham(binary_vector, dcount_vectors: pd.DataFrame):
    vocab = binary_vector[0]
    print(vocab)
    vectors = binary_vector[1].astype(int)
    print(sum(vectors))

    ham_df = dcount_vectors.loc[dcount_vectors["Doc_Class"] == "ham"]
    spam_df = dcount_vectors.loc[dcount_vectors["Doc_Class"] == "spam"]

    num_of_spams = len(spam_df)
    num_of_hams = len(ham_df)
    num_of_docs = len(dcount_vectors)
    prob_spam = num_of_spams / num_of_docs
    prob_ham = num_of_hams / num_of_docs

    list_of_log_prob_spam = []
    list_of_log_prob_ham = []
    for index, word in enumerate(vocab):
        if vectors[index] == 1:
            print(word, vectors[index])
            num_of_docs_with_word_ham = (ham_df[word] != 0).sum()
            num_of_docs_with_word_spam = (spam_df[word] != 0).sum()

            if (
                num_of_docs_with_word_ham == 0
                or num_of_docs_with_word_spam == 0
            ):
                num_of_docs_with_word_spam += 1
                num_of_docs_with_word_ham += 1

            prob_word_indicates_spam = np.log(
                num_of_docs_with_word_spam / num_of_spams
            )
            prob_word_indicates_ham = np.log(
                num_of_docs_with_word_ham / num_of_hams
            )

            list_of_log_prob_spam.append(prob_word_indicates_spam)
            list_of_log_prob_ham.append(prob_word_indicates_ham)

    print(sum(list_of_log_prob_ham))
    print(sum(list_of_log_prob_spam))
    prob_log_sum_exp_ham = math.exp(sum(list_of_log_prob_ham))
    prob_log_sum_exp_spam = math.exp(sum(list_of_log_prob_spam))
    print(prob_log_sum_exp_ham)
    print(prob_log_sum_exp_spam)


def generate_vocabulary(documents):
    tokens = []
    print(documents[0])
    for doc in documents:
        tokens.extend(tokenize(doc))
    fdist = nltk.FreqDist(tokens)
    unique_words = list((dict(fdist).keys()))

    vocabulary = "\n".join(unique_words)

    with open("training_vocab.txt", "w", encoding="utf-8") as f:
        f.write(vocabulary)

    f.close()


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

    binary_vector = generate_binary_vector(all_docs[1], vocab)
    dcount_vectors = generate_dcount_vectors(vocab, documents)
    classify_spam_ham(binary_vector, dcount_vectors)
