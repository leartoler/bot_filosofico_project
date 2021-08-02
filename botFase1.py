import tweepy, re, time, nltk
from nltk.util import ngrams
from access_tfbot import *
from random import randint
from nltk.corpus import stopwords

libros = ["texto.txt","texto2.txt"]
randomBook = randint(0,len(libros)-1)
randomBook = libros[randomBook]
stopwd = stopwords.words('english')
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
	#genera un numero aleatorio
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
					wordNgram = []
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
					orderedWords = sorted(set(words))
                    #definimos lista de trigramas del texto del tweet y los imprimimos
					trigrams = list(ngrams(words,3))
					print("tweet en trigramas",trigrams,"\n")
                    #verifica que la palabra a buscar "randomWord" esté cada elemento de la lista de trigramas
					for trigram in trigrams:
						#print(trigram,"\n")
						if randomWord in trigram:
                            
							print(f"trigramas que incluyen {randomWord} ",trigram,"\n")
	                    #si es así, agrega el trigrama a la lista "wordNgram"
							wordNgram.append(trigram)
#							print(wordNgram)
# 						#print(randomWord, "\n", orderedWords, "\n")
						else:
							pass
# 								search_word_tweet(api)
					data.update({"word_searched":randomWord,"tweet_found":tweetxt,"tweet_found_tokens":tokens,"twt_found_ordered_tokens":orderedWords,"random_word_in_trigram":wordNgram})
					tweeting(api,randomWord,wordNgram,url)
					return randomWord, url, wordNgram

def tweeting(api,randomWord,wordNgram,url):
		checkNgram = []
		status = extract_status(randomBook)
		#tokenizamos el texto a enviar mayor a tres caracteres"
		status_tokens = nltk.tokenize.word_tokenize(status)
		status_tokens = [word for word in status_tokens if word not in stopwd]
		print("status tokenizado",status_tokens,"\n")
		if randomWord in status_tokens:
			trigramStatus = list(ngrams(status_tokens,3))
			print("status organizado en trigramas",trigramStatus,"\n")
        #si la palabra a buscar está en el texto tokenizado seleccionado de la data base, enviar tweet como retweet citado
			for trig in trigramStatus:
				if randomWord in trig:
					print("trigramamamammamama",trig,"\n")
					checkNgram.append(trig)
					try:
						api.update_status(status +" " + url)
						data.update({"txt_sended":status,"txt_sended_tokens":status_tokens,"word_in_twt_trigrams":checkNgram})
						writing_db()
						print(f"{status} \n Tweet enviado!")
						print("funciona")
						break
					except tweepy.TweepError as e:
						print(e.reason)
				else:
					pass
		else:
			tweeting(api, randomWord, wordNgram, url)
		return status, status_tokens, checkNgram


if __name__ == '__main__':
	#configurar API de twitter
	bot = twitter_setup()
	#delay
	segs = 600
	while True:
		search_word_tweet(bot)
		break#time.sleep(segs)

