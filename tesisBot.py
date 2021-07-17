import requests, json
from random import randint

#hacemos una petición a la api via http y guardamos la db en formato json
api = requests.get('http://tesis.filos.unam.mx/api/theses')
api = api.json()
total = api['total']
tesis_db = api['data']

rand = randint(1, len(tesis_db))
tesisRandom = tesis_db[rand]
keywords = tesisRandom['keywords']
url = tesisRandom['rawData']['file']
author = tesisRandom['rawData']['author']
title = tesisRandom['rawData']['title']
year = tesisRandom['rawData']['year']

print(f"Tesis del año {year} titulada \"{title}\", escrita por {author}. la puedes consultar en {url}")