import tweepy, re, time, nltk
from access_tfbot import *
from random import randint

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
	#genera un numero aleatorio
		index = randint(0, len(text))
	#determina indices de la oracion
		init_index = text[index:].find(".") + 2 + index
		last_index = text[init_index:].find(".") + 2 + index
		status = len(text[init_index:last_index])
	#remplaza cualquier caracter que no sea palabra y numero de linea con espacios
	sentence = text[init_index:last_index]
	sentence = re.sub("\W\d", " ", sentence)
	return sentence

if __name__ == '__main__':
		#configurar API de twitter
		bot = twitter_setup()
        #definimos conjunto de palabras a buscar
        #enviamos el indice aleatorio de un elemento del conjunto definido arriba
		setWords = ["technology", "tech", "technical", "information", "tecnologia", "tecnica", "tecnologico", "informacion"]
		randomWord = randint(0,len(setWords)-1)
		randomWord = setWords[randomWord]
		#delay
		segs = 1
		#switch
		switch= False
		#buscamos una palabra aleatoria definida anteriormente e iteramos este proceso n veces en count
        #devolvemos un array con los tweets encontrados
		searchWord = bot.search(q=randomWord, count=1)
		count = 0
		status = extract_status("texto.txt")
		#iteramos sobre el array de busqueda
        #definimos un patron con regex para tokenizar el tweet
        #imprimimos el numero de iteracion junto con el texto del tweet y el conjunto ordenado de los tokens del tweet
		for tweet in searchWord:
					tweet = tweet.text
					pattern = r'''(?x)                 # set flag to allow verbose regexps
              (?:[A-Z]\.)+         # abbreviations, e.g. U.S.A.
              | \w+(?:-\w+)*       # words with optional internal hyphens
              | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
              | \.\.\.             # ellipsis
              | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
'''
					tokens = nltk.regexp_tokenize(tweet, pattern)
					print(f"{count}, {tweet}")
					print(sorted(set(tokens)))
#					count += 1
#					switch = True
#			#control de flujo para postear tuits
#					while switch:
	
#						try:
#							bot.update_status(status +" " + f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
#							print(f"{status} \n Tweet enviado!")
#							switch = False
#						except tweepy.TweepError as e:
# 							print(e.reason)

		time.sleep(segs)

