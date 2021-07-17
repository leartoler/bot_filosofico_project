import tweepy, time, json, nltk
from nltk.util import ngrams
from access import *
from random import randint
#from random import randint

# Setup API:
def twitter_setup():
    # Authenticate and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API access:
    api = tweepy.API(auth)
    return api

if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()


    secs = 1
    


    #  tweetlist = ["lol",
    #               "trololol",
    #               "a"]

    
    #  for tweet in tweetlist:
  
    #      print(tweet)

        
    #      try:
    # #funcion para subir un tweet    
    #          bot.update_status(tweet)
    #          print("Tweet enviado!")
    #      except tweepy.TweepError as e:
    #          print(e.reason)
    #hacer una busqueda
    setWords = ["technology", "tech", "technical", "information", "technological"]
    randomWord = randint(0,len(setWords)-1)
    randomWord = setWords[randomWord]
    print(randomWord,"\n")
    tw = bot.search(q=randomWord, count=1)
    #imprimir ultimos 10 tw del feed
    public_tweets = bot.home_timeline(count=1)

    count = 0
def testing():

        for tweet in tw:
            #print("", json.dumps(tweet._json, indent=2))
            #print(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
            #print(f"{count}. {tweet}")
            wordNgram = []
            tokens = nltk.tokenize.word_tokenize(tweet.text)
            print(tokens)
            words = [word for word in tokens if len(word) > 2]
            trigrams = list(ngrams(words,3))
            for trigram in trigrams:
                if randomWord in trigram:
                    wordNgram.append(trigram)
                    print(trigram)
                    
            return wordNgram
testing()
        #count+=1
        # Wait till next sentence extraction:

    