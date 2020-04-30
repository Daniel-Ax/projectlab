from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import API_keys

class StdOutListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)

if __name__=='__main__':
    listener=StdOutListener()
    auth=OAuthHandler(API_keys.CONSUMER_KEY,API_keys.CONSUMER_SECRET)
    auth.set_access_token(API_keys.ACCESS_TOKEN,API_keys.ACCESS_TOKEN_SECRET)
    stream=Stream(auth,listener)
