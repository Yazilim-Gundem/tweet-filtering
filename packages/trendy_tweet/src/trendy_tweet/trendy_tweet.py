# -*- coding: utf-8 -*-
""" trendy_tweet.py """
__author__ = 'abdullahbozdag'
__creation_date__ = '17.02.2023'

import datetime

import snscrape.modules.twitter as sc_twitter


class TrendyTweet:
    def __init__(self, usernames: list, since: datetime, until: datetime, limit: int = 100,
                 filter_query: str = '-filter:replies'):
        self.usernames = usernames
        self.since = since
        self.until = until
        self.limit = limit
        self.filter_query = filter_query

    def get_tweets(self) -> list[dict]:
        username_text_query_list = []
        twitter_search_query = f'until:{self.until} since:{self.since} {self.filter_query}'
        for i in range(0, len(self.usernames), 20):
            username_text_query_list.append(' OR from:'.join(self.usernames[i:i + 20]))

        tweets_list = []
        for username_text_query in username_text_query_list:
            tweets = sc_twitter.TwitterSearchScraper(
                f'(from:{username_text_query}) {twitter_search_query}'
            ).get_items()
            for index, tweet in enumerate(tweets):
                if index >= self.limit:
                    break
                view_count = tweet.viewCount if tweet.viewCount else 0
                mentioned_users = [
                    user.username for user in tweet.mentionedUsers
                ] if tweet.mentionedUsers else []
                in_reply_to_user = tweet.inReplyToUser.username if tweet.inReplyToUser else None
                tweets_list.append({
                    'username': tweet.user.username,
                    'created': tweet.date.strftime("%Y-%m-%d %H:%M:%S"),
                    'number_of_likes': tweet.likeCount,
                    'retweet_count': tweet.retweetCount,
                    'quote_count': tweet.quoteCount,
                    'reply_count': tweet.replyCount,
                    'view_count': view_count,
                    'mentioned_users': mentioned_users,
                    'in_reply_to_user': in_reply_to_user,
                    'lang': tweet.lang,
                    'source_of_tweet': tweet.sourceLabel,
                    'tweet_content': tweet.content,
                    'url': tweet.url
                })

        return tweets_list
