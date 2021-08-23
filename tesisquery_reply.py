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
    for mention in mentions:
        if "tesis relacionada" in mention.text:
            text_split = mention.text.split("@_TFbot tesis relacionada con ")
            print(f"{mention.text} \n {str(text_split)}")
            tokens = nltk.tokenize.word_tokenize(str(text_split))
            print(tokens)
            def selectTesis():
                tesis = randomThesis()
                keywords = tesis[5]
                print(keywords)
                for token in tokens:
                    if token in keywords:
                        tesis = filtrarThesis(tesis)
                        print(tesis)
                        return tesis
                    else:
                        selectTesis()
            tesis = selectTesis()
            return tesis



if __name__ == '__main__':

    bot = twitter_setup()
    mentions = bot.mentions_timeline()
    reply = replyQuery(bot)
    #bot.update_status(reply)
    print(f"Respuesta enviada: {reply}")