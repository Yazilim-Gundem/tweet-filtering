# -*- coding: utf-8 -*-
""" main """
__author__ = 'abdullahbozdag'
__creation_date__ = '17.02.2023'

import datetime
import json

import pandas as pd
from helpers import usernames, labels, translate
from packages.trendy_tweet.src.trendy_tweet.trendy_tweet import TrendyTweet
from packages.tweet_classification.src.tweet_classification.tweet_classification import \
    TweetClassification


def get_tweets(save_csv: bool = False) -> list:
    until_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    since_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    get_usernames = usernames()

    tt = TrendyTweet(get_usernames, since_date, until_date)
    tweets = tt.get_tweets()

    filtered_tweets = [
        tweet_item for tweet_item in tweets if
        tweet_item['lang'] in ['tr', 'en'] and tweet_item['view_count'] > 7000 and tweet_item[
            'number_of_likes'] > 10
    ]
    if save_csv:
        tweets_df = pd.DataFrame(
            filtered_tweets,
            columns=[
                'username', 'created', 'number_of_likes', 'retweet_count', 'quote_count',
                'reply_count', 'view_count', 'mentioned_users', 'in_reply_to_user', 'lang',
                'source_of_tweet', 'tweet_content', 'url'
            ]
        )
        tweets_df.to_csv('tweets.csv', index=False)

    return filtered_tweets


def tweet_classification(tweet_content: str) -> dict:
    tweet_classification_cls = TweetClassification()
    get_labels = labels()

    classification_result = tweet_classification_cls.classify(
        sentence=tweet_content, labels=get_labels, multi_label=1
    )

    # r_sequence = classification_result["sequence"]
    r_labels = classification_result["labels"]
    r_scores = classification_result["scores"]

    return dict(zip(r_labels, r_scores))


if __name__ == '__main__':
    share_tweet_list = []
    for tweet in get_tweets():
        content = tweet['tweet_content']
        mentioned_users = tweet['mentioned_users']
        lang = tweet['lang']
        url = tweet['url']
        if lang == 'tr':
            content = translate(text=content, target_language='en')
        result_classification = tweet_classification(tweet_content=content)

        first_3 = sorted(result_classification.items(), key=lambda x: x[1], reverse=True)[:3]

        featured_labels = [
            'software', 'hardware', 'game', 'company', 'brand', 'phone', 'programming', 'tool'
        ]
        if any([x[0] in featured_labels for x in first_3]):
            share_tweet_list.append({
                'url': url,
                'mentioned_users': mentioned_users,
                'featured_labels': dict(first_3),
                'ss': f'https://tweet-to-image-smoky.vercel.app/?tweet={url}'
            })

    with open('result.json', 'w') as f:
        f.write(json.dumps(share_tweet_list))
