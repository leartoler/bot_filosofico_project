#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: dgrm
"""

from nltk.sem.evaluate import Undefined
import requests, json, tweepy, nltk, re
from botFase1 import *
from random import randint

#hacemos una petición a la api via http y guardamos la db en formato json
api = requests.get('http://tesis.filos.unam.mx/api/theses?limit=0')
api = api.json()
total = api['total']
tesis_db = api['data']
#definimos funcion para seleccionar una tesis al azar
def randomThesis():
#tomamos una tesis al azar y guardamos algunos campos
    rand = randint(1, len(tesis_db))
    tesisRandom = tesis_db[rand]
    keywords = tesisRandom['keywords']
    url = tesisRandom['rawData']['file']
    #convertir el orden del nombre del autor de apellidos, nombre a nombre apellidos
    #tokenizamos, invertimos y filtramos caracteres no significativos como "," etc
    author = tesisRandom['author']
    author = nltk.tokenize.word_tokenize(author)
    author = [i for i in author if len(i) > 1][::-1]
    author = re.sub("\W"," ",str(author))
    author = "".join(author)
    author = re.sub("[  ]+"," ",author)
    title = tesisRandom['title']
    year = tesisRandom['rawData']['year']
    grade = tesisRandom['degree']
    return url, author, title, year, grade, keywords

#definimos funcion para el filtrado de tesis
def filtrarThesis(url, author, title, year, grade,keywords):
    try:
        text = f"Tesis del año {year} titulada \"{title}\", escrita por{author} para obtener el grado en {grade}. La puedes consultar en {url}"
        if len(text) > 255:
            text = f"{author} ({year}) \"{title}\".\n {url}"
    except:
        text = f"Tesis del año {year} titulada \"{title}\", escrita por{author} para obtener el grado en {grade}."
        
    return text

#definimos funcion para retweet
def retwt():
    tfBot_timeLine = bot.user_timeline()
    lastTwt_id = tfBot_timeLine[0].id
    tfBot = tfBot_timeLine[0].user.screen_name
    rt = f"#SeminarioTF #TesisFilosUNAM https://twitter.com/{tfBot}/status/{lastTwt_id}"
    bot.update_status(rt)

if __name__ == '__main__':
    segs = 600
    bot = twitter_setup()
    while True:
        url, author, title, year, grade, keywords = randomThesis()
        tesis = filtrarThesis(url, author, title, year, grade,keywords)
        bot.update_status(tesis)
        print(f'Tuit enviado: {tesis}')
        time.sleep(30)
        retwt()
        print("Retweet enviado!")
        time.sleep(segs)
