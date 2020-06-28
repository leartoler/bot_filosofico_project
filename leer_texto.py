import tweepy, re, time
from access import *
from random import randint

# Setup API:
def twitter_setup():
    # Authenticate and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API access:
    api = tweepy.API(auth)
    return api

#función para extraer status 
def extract_status(path=None):
    	if not path:
    		return "No hay libro"

    	#busca libro que leer y oración 
    	try: 
    		with open(path, 'r', encoding='utf-8', errors="surrogateescape") as book:
    			text = book.read()

    		#si la lee exitosamente el libro, busca una oración
    		if text:
    			return search_sentence(text)

    	except:
    		return "libro no encontrado"

#función para determinar búsqueda de oración en el libro
def search_sentence(text): 
	status = 200


	#mientras tengamos un status largo o muy corto
	while not (5 < status < 125):
	#genera un número aleatorio
		index = randint(0, len(text))
	#determina índices de la oración
		init_index = text[index:].find(".") + 2 + index
		last_index = text[init_index:].find(".") + 2 + index
		status = len(text[init_index:last_index])
	#remplaza saltos de línea con espacios
	sentence = text[init_index:last_index]
	sentence = re.sub("\n", " ", sentence)
	return sentence

	if __name__ == '__main__':
		#configurar API de twitter
		bot = twitter_setup()

		#delay
		segs = 3 

		#control de flujo para postear tuits
		while True: 
			status = extract_status("texto.txt")

			try:
            	bot.update_status(tweet)
            	print("Tweet enviado!")
        	except tweepy.TweepError as e:
            	print(e.reason)

      		time.sleep(segs)

