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
    rand = randint(1, len(tesis_db)-1)
    tesisRandom = tesis_db[rand]
    keywords = tesisRandom['keywords']
    try:
        url = tesisRandom['rawData']['file'] 
    except:
        url = Undefined
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
def filtrarThesis(randomThesis):
    if randomThesis[0] != Undefined:
        text = f"Tesis del año {randomThesis[3]} titulada \"{randomThesis[2]}\", escrita por{randomThesis[1]} para obtener el grado en {randomThesis[4]}. La puedes consultar en {randomThesis[0]}"
        if len(text) > 255:
            text = f"{randomThesis[1]} ({randomThesis[3]}) \"{randomThesis[2]}\".\n {randomThesis[0]}"
    else:
        text = f"Tesis del año {randomThesis[3]} titulada \"{randomThesis[2]}\", escrita por{randomThesis[1]} para obtener el grado en {randomThesis[4]}."
        
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
        tesis_tupla = randomThesis()
        tesis = filtrarThesis(tesis_tupla)
        #bot.update_status(tesis)
        print(f'Tuit enviado: {tesis}')
        time.sleep(30)
        #retwt()
        #print("Retweet enviado!")
        time.sleep(segs)
