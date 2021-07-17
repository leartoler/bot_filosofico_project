import requests, json

#hacemos una petición a la api via http y guardamos la db en formato json
api = requests.get('http://tesis.filos.unam.mx/api/theses')
api = api.json()
total = api['total']
tesis_db = api['data']