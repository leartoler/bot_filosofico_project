import tweepy, time
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

if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()


    secs = 180

semibot
    tweetlist = ["tuit de prueba 1",
                "tuit de prueba 2",
                "tuit de prueba 3"]

    
    for tweet in tweetlist:
  
        print(tweet)

        
        try:
            bot.update_status(tweet)
            print("Tweet enviado!")
        except tweepy.TweepError as e:
            print(e.reason)


        # Wait till next sentence extraction:
        time.sleep(secs)
