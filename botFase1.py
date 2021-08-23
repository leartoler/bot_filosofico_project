#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: dgrm
"""

import tweepy, re, time, nltk
from nltk.util import ngrams
from access_tfbot import *
from random import randint
from nltk.corpus import stopwords
from nltk.probability import FreqDist

#se definen algunas variables globales
libros = ["texto.txt","texto2.txt"]
randomBook = randint(0,len(libros)-1)
randomBook = libros[randomBook]
#se definen stopwords para facilitar limpieza con nltk
stopwd = stopwords.words('english')
#creamos un diccionario vacio para guardar datos del bot
#y enviarlos a una base de datos en mongodb para futuros usos
data = {}

def writing_db():
	with open("./db/data.py",mode="a", encoding="utf-8", errors="surrogateescape") as db:
		db.write("collection.insert_one(")
		db.write(str(data))
		db.write(")")
		db.write("\n")


# Setup API:
def twitter_setup():
	# Authenticate and access using keys:
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	# Return API access:
	api = tweepy.API(auth)
	return api

#funcion para extraer status 
def extract_status(path=None):
		if not path:
			return "No hay libro"

		#busca libro que leer y oracion 
		try: 
			with open(path, 'r', encoding='utf-8', errors="surrogateescape") as book:
				text = book.read()

			#si la lee exitosamente el libro, busca una oracion
			if text:
				return search_sentence(text)

		except:
			return "libro no encontrado"

#funcion para determinar busqueda de oracion en el libro
def search_sentence(text): 
	status = 250

	#mientras tengamos un status largo o muy corto
	while not (5 < status < 225):
	#genera un numero aleatorio para definir un indice
		index = randint(0, len(text))
	#determina indices de la oracion
		init_index = text[index:].find(".") + 2 + index
		last_index = text[init_index:].find(".") + 2 + index
		status = len(text[init_index:last_index])
	#remplaza cualquier caracter que no sea palabra y numero de linea con espacios
	sentence = text[init_index:last_index]
	sentence = re.sub("\W\d\n\t—[0-9],,.", " ", sentence)
	sentence = re.sub("-","",sentence)
	return sentence

#funcion que busca una palabra de setWords en Twitter para construir un tweet en consecuencia
def search_word_tweet(api):
        #definimos conjunto de palabras a buscar
        #enviamos el indice aleatorio de un elemento del conjunto definido arriba
		setWords = ["technology", "tech",
			"technical", "information",
			"informational", "technological",
			"artificial intelillence",
			"device", "tool",
			"ai", "algorithm",
			"instrument"]
		randomWord = randint(0,len(setWords)-1)
		randomWord = setWords[randomWord]
		#buscamos una palabra aleatoria definida anteriormente e iteramos este proceso n veces en count
        #devolvemos una lista con los tweets encontrados
		searchTweet = api.search(q=randomWord, count=1)
		#iteramos sobre la lista de tweets encontrados
        #definimos un patron con regex para tokenizar el tweet
        #imprimimos el numero de iteracion junto con el texto del tweet y el conjunto ordenado de los tokens del tweet mayores a 3 caracteres
		for tweet in searchTweet:
					url = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
					tweetxt = tweet.text.lower()
					pattern = r'''(?x)                 # set flag to allow verbose regexps
              (?:[A-Z]\.)+         # abbreviations, e.g. U.S.A.
              | \w+(?:-\w+)*       # words with optional internal hyphens
              | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
              | \.\.\.             # ellipsis
              | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
'''
					tokens = nltk.regexp_tokenize(tweetxt, pattern)
					print(f"tweet con {randomWord} encontrado: {tweetxt} \n")
					words = [word for word in tokens if word not in stopwd]
                    #sacamos frecuencia de palabras filtradas
					freqs = FreqDist(words)
					freqs = {key: value for key, value in freqs.items()}
					orderedWords = sorted(set(words))
                    #llamamos a la funcion ngrammatize para hacer ngramas
                    #con los tokens del tweet, verificando que randomWord
                    #(o la palabra a buscar) pertenece a todos y c/u de los ngramas
					wordNgram = ngrammatize(words, randomWord, api, url)
					print(f"frecuencias: {freqs}\n {randomWord} en los n-gramas del tweet")
					data.update({"word_searched":randomWord,"tweet_found":tweetxt,"tweet_found_tokens":words,"frecuencia_tokens":freqs,"twt_found_ordered_tokens":orderedWords,"random_word_in_ngrams_twt":wordNgram})
					tweet_constructor(api,randomWord,url)
					return randomWord, url, words

#funcion que construye el tweet a enviar
def tweet_constructor(api,randomWord,url):
		status = extract_status(randomBook)
		#tokenizamos el texto a enviar mayor a tres caracteres"
		status_tokens = nltk.tokenize.word_tokenize(status)
		status_tokens = [word for word in status_tokens if word not in stopwd]
		freqs = FreqDist(status_tokens)
		freqs = {key: value for key, value in freqs.items()}
		if randomWord in status_tokens:
			checkNgram = ngrammatize(status_tokens, randomWord, api, url)
			print(f"status tokenizado {status_tokens}\n frecuencias: {freqs}\n {randomWord} en n-gramas del texto: {checkNgram}")
			send_twt(api, status, url)
			data.update({"txt_sended":status,"txt_sended_tokens":status_tokens,"frecuencias_tokens":freqs,"word_in_ngrams_twt_sended":checkNgram})
		else:
			tweet_constructor(api, randomWord, url)
		return status, status_tokens

#función que envia tweet
def send_twt(api, status, url): 
		try:
			#api.update_status(status +" " + url)
			print(f"{status} \n Tweet enviado!")
			print("funciona")
		except tweepy.TweepError as e:
			print(e.reason)

#funcion que ngramatiza un texto de entrada que incluya randomWord
#retorna un diccionario con todos los ngramas como valor 
def ngrammatize(words, randomWord, api, url):
	len_tokens = len(words)
	nGrams = []
	word_in_Ngrams = {}
    #si la randomWord esta en la lista de tokens, el bot hara 
    #una lista con todos los ngramas posibles del texto de entrada
	if randomWord in words:
		for x in range(1,len_tokens-1):
			ngramGroup = list(ngrams(words, x))
			nGrams.append(ngramGroup)
    #creamos lista filtrada con los ngramas que incluyen randomWord como elemento
		ngramas = [elemento for ngrama in nGrams for elemento in ngrama if randomWord in elemento]
		print(f"Lista de ngramas que incluyen {randomWord}:\n{ngramas}\n Un total de {len(ngramas)} n-gramas\n")
		word_in_Ngrams.update({"ngramas":ngramas})
	else:
		search_word_tweet(api)
	return word_in_Ngrams

if __name__ == '__main__':
	#configurar API de twitter
	bot = twitter_setup()
	#delays
	segs = 600
	while True:
		search_word_tweet(bot)
		break#time.sleep(segs)

