#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:55:37 2021

@author: dgrm
"""
import requests, json, tweepy, nltk, re
from botFase1 import *
from tesisBot import *

#variables tw


def replyQuery(bot):
    for i in mentions:
        if "tesis relacionada" in i.text:
            url, author, title, year, grade, keywords = randomThesis()
            tesis = filtrarThesis(url,author,title,year,grade,keywords)
            tokens = nltk.tokenize.word_tokenize(i.text)
            for i in tokens:
                if i in keywords:
                    print(tesis)
                    return tesis
                else:
                    replyQuery(bot)
                    print("algo raro")


if __name__ == '__main__':

    bot = twitter_setup()
    mentions = bot.mentions_timeline()
    reply = replyQuery(bot)
    bot.update_status(reply)
    print(f"Respuesta enviada: {reply}")