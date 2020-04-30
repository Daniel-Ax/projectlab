from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import API_keys

class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(API_keys.CONSUMER_KEY, API_keys.CONSUMER_SECRET)
        auth.set_access_token(API_keys.ACCESS_TOKEN, API_keys.ACCESS_TOKEN_SECRET)
        return auth

class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator=TwitterAuthenticator()

    def stream_tweets(self, tweet_filename, hashtag_list):
        #Ez kezeli a twitter azonosítást és a Twitter streamer API-t
        listener = TwitterListener()
        auth = OAuthHandler(API_keys.CONSUMER_KEY, API_keys.CONSUMER_SECRET)
        auth.set_access_token(API_keys.ACCESS_TOKEN, API_keys.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream=self.twitter_authenticator.authenticate_twitter_app()
        stream.filter(track=hashtag_list)

class TwitterListener(StreamListener):
    #Alap listener osztály
    def __init__(self,tweet_filename):
        self.tweet_filename=tweet_filename

    def on_data(self, raw_data):
        try:
            print(raw_data)
            with open(self.tweet_filename,'a') as tf:
                tf.write(raw_data)
                return True
        except BaseException as e:
            print("Error data:",str(e))
            return True

    def on_error(self, status_code):
        print(status_code)

if __name__=='__main__':
    hashtag_list=['donald trump','barack obama']
    tweet_filename="tweets.json"
    twitter_streamer=TwitterStreamer()
    twitter_streamer.stream_tweets(tweet_filename,hashtag_list)
