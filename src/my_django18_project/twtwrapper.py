import requests
from twython import Twython
import json

from django.conf import settings
from .settings import twt_APP_KEY, twt_APP_SECRET, twt_OAUTH_TOKEN, twt_OAUTH_TOKEN_SECRET
import os


class TWT(object):

    APP_KEY = twt_APP_KEY
    APP_SECRET = twt_APP_SECRET
    OAUTH_TOKEN = twt_OAUTH_TOKEN
    OAUTH_TOKEN_SECRET = twt_OAUTH_TOKEN_SECRET
    

    def __init__(self):
        super(TWT, self).__init__()

    @staticmethod
    def find(name):
        twitter = Twython(TWT.APP_KEY, TWT.APP_SECRET, TWT.OAUTH_TOKEN, TWT.OAUTH_TOKEN_SECRET)
        ts = twitter.search(q=name, lang = 'en', result_type = 'recent')
        tl = []
        for tweet in ts['statuses']:
            tl.append({'name': tweet['text'], 'score': 5 })

        return tl

