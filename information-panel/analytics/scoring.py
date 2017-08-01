"""Scoring, analysing

    This file includes functions to analyse the tweets and
    give them scores.
"""
import re
import os


def get_words():
    """Get words

        Returns a list with first a list of positive words
        and second a list of negative words.
    """
    # path to the directory including the word-files
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\src\\"

    # reading in the positive and negative words as lists
    pos_words = []
    neg_words = []
    with open(dir_path + "positive-words.txt") as positive, open(dir_path + "negative-words.txt") as negative:
        for line in positive:
            li = line.strip()
            if not li.startswith(";"):
                pos_words.append(line.rstrip())
        for line in negative:
            li = line.strip()
            if not li.startswith(";"):
                neg_words.append(line.rstrip())

    return [pos_words, neg_words]


def scoring(tweets):
    """Scoring

        Returns a dictionary containing the tweets as keys and the
        scoring as their values.
    """
    scored_tweets = {}
    for tweet in tweets:
        # removing unwanted parts
        tweet = re.sub('https://', '', tweet)
        tweet = re.sub('http://', '', tweet)
        tweet = re.sub('[^[:graph:]]', ' ', tweet)
        tweet = re.sub('[[:punct:]]', '', tweet)
        tweet = re.sub('[[:cntrl:]]', '', tweet)
        tweet = re.sub('\\d+', '', tweet)
        tweet = re.sub('#', '', tweet)
        tweet = re.sub('\u2026', '', tweet)

        tweet = tweet.lower()

        # split to a list of words
        tweet_list = tweet.split()

        # getting words for scoring
        words = get_words()
        pos_words = words[0]
        neg_words = words[1]

        # defining the score
        pos_matches = 0
        neg_matches = 0
        for pos, neg in zip(pos_words, neg_words):
            pos_matches += tweet_list.count(pos)
            neg_matches += tweet_list.count(neg)
        
        scored_tweets.update({tweet : pos_matches - neg_matches})
    
    return scored_tweets

