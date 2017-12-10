import requests
from twython import Twython
import json
import string
from nltk.corpus import stopwords
from django.conf import settings
from .settings import SCORES_FOLDER, twt_APP_KEY, twt_APP_SECRET, twt_OAUTH_TOKEN, twt_OAUTH_TOKEN_SECRET
import os


class TWT(object):

    APP_KEY = twt_APP_KEY
    APP_SECRET = twt_APP_SECRET
    OAUTH_TOKEN = twt_OAUTH_TOKEN
    OAUTH_TOKEN_SECRET = twt_OAUTH_TOKEN_SECRET
    
    scores = {} 
    with open(  os.path.join(SCORES_FOLDER,"AFINN-111.txt"), "r") as sent_file:
        for line in sent_file:
            term, score = line.split("\t")
            scores[term] = int(score)

    def __init__(self):
        super(TWT, self).__init__()

    @staticmethod
    def find(name):
        twitter = Twython(TWT.APP_KEY, TWT.APP_SECRET, TWT.OAUTH_TOKEN, TWT.OAUTH_TOKEN_SECRET)
        ts = twitter.search(q=name, count=200, lang = 'en', result_type = 'recent')
        tl = []
        s = []
        for tweet in ts['statuses']:
            if tweet['text'] not in s:
                tl.append({'name': tweet['text'], 'score': scoreTweet(tweet) })
                s.append(tweet['text'])
        return tl

#Gets the text, sans links, hashtags, mentions, media, and symbols.
def get_text_cleaned(tweet):
    text = tweet['text']        
    slices = []
    #Strip out the urls.
    if 'urls' in tweet['entities']:
        for url in tweet['entities']['urls']:
            slices += [{'start': url['indices'][0], 'stop': url['indices'][1]}]        
    #Strip out the hashtags.
    if 'hashtags' in tweet['entities']:
        for tag in tweet['entities']['hashtags']:
            slices += [{'start': tag['indices'][0], 'stop': tag['indices'][1]}]        
    #Strip out the user mentions.
    if 'user_mentions' in tweet['entities']:
        for men in tweet['entities']['user_mentions']:
            slices += [{'start': men['indices'][0], 'stop': men['indices'][1]}]        
    #Strip out the media.
    if 'media' in tweet['entities']:
        for med in tweet['entities']['media']:
            slices += [{'start': med['indices'][0], 'stop': med['indices'][1]}]        
    #Strip out the symbols.
    if 'symbols' in tweet['entities']:
        for sym in tweet['entities']['symbols']:
            slices += [{'start': sym['indices'][0], 'stop': sym['indices'][1]}]        
    # Sort the slices from highest start to lowest.
    slices = sorted(slices, key=lambda x: -x['start'])        
    #No offsets, since we're sorted from highest to lowest.
    for s in slices:
        text = text[:s['start']] + text[s['stop']:]            
    return text    
#Sanitizes the text by removing front and end punctuation, 
#making words lower case, and removing any empty strings.
def get_text_sanitized(tweet):    
    return ' '.join([w.lower().strip().rstrip(string.punctuation)\
        .lstrip(string.punctuation).strip()\
        for w in get_text_cleaned(tweet).split()\
        if w.strip().rstrip(string.punctuation).strip()])    
#Gets the text, clean it, make it lower case, stem the words, and split
#into a vector. Also, remove stop words.
def scoreTweet(tweet):
    #Sanitize the text first.
    text = get_text_sanitized(tweet).split()        
    #Remove the stop words.
    text = [t for t in text if t not in stopwords.words('english')]        
    tweet_score = 0
    for word in text:
        word = word.encode('utf-8')
        word_score = int(TWT.scores.get(word,'0'))
        tweet_score = tweet_score + word_score
    return tweet_score      
