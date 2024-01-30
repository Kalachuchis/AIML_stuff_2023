import requests
import json
import csv
import pandas as pd
import random


def create_csv(data, name):
    print("Creating csv file")
    data_file = open(f"{name}.csv", "w")

    csv_writer = csv.writer(data_file)

    headers_written = False

    print("writing to csv")
    for row in data:
        if not headers_written:

            headers = row.keys()
            csv_writer.writerow(headers)
            headers_written = True
        csv_writer.writerow(row.values())


if __name__ == "__main__":
    todo_data = {"userID": 1, "title": "Kain pepe", "completed": True}
    headers = {"Content-Type": "application/json"}

    comments_url = "https://jsonplaceholder.typicode.com/comments"
    posts_url = "https://jsonplaceholder.typicode.com/posts"

    # response = requests.get(api_url)

    response = requests.get(comments_url)
    comments = response.json()

    response = requests.get(posts_url)
    posts = response.json()

    create_csv(comments, "comments")
    create_csv(posts, "posts")

    random_list = random.sample(range(1, 100), 20)

    comments_df = pd.read_csv('./comments.csv')
    posts_df = pd.read_csv('./posts.csv')

    random_posts = posts_df.iloc[random_list]
    print("list id")
    random_post_ids = random_posts['id'].to_list()
    print(random_post_ids)

    random_comments = comments_df.loc[comments_df["id"].isin(random_post_ids)]
    print(random_comments)
    comments_df.loc[comments_df["id"].isin(
        random_post_ids), 'body'] = random_posts.loc[random_posts['id'].isin(random_post_ids), 'body']

    random_comments = comments_df.loc[comments_df["id"].isin(random_post_ids)]
    print("new comments")
    print(random_comments)

    comments_df.to_csv("modified_comments.csv")
