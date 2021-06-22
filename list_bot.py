import tweepy, time
from access import *
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


    secs = 180


     tweetlist = ["lol",
                  "trololol",
                  "a"]

    
     for tweet in tweetlist:
  
         print(tweet)

        
         try:
    #funcion para subir un tweet    
             bot.update_status(tweet)
             print("Tweet enviado!")
         except tweepy.TweepError as e:
             print(e.reason)
    #hacer una busqueda
    #tw = bot.search(q="tech")
    #imprimir ultimos 10 tw del feed
    #public_tweets = bot.home_timeline(count=10)

    #count = 0
		
    #for tweet in public_tweets:
    #    print("")
    #    print(f"{count}. {tweet.text}")
    #    count+=1
        # Wait till next sentence extraction:
    time.sleep(secs)
    