from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import API_keys
import numpy as np
import pandas as pd


class TwitterClient():
    def __init__(self,twitter_user=None):
        self.auth=TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_clent=API(self.auth)
        self.twitter_user=twitter_user

    def get_twitter_client_api(self):
        return self.twitter_clent

    def get_user_timeline_tweets(self,num_tweets):
        my_tweets=[]
        for tweet in Cursor(self.twitter_clent.user_timeline,id=self.twitter_user).items(num_tweets):
            my_tweets.append(tweet)
        return my_tweets
    def get_friend_list(self,num_friends):
        friends=[]
        for friend in Cursor(self.twitter_clent.friends,id=self.twitter_user).items(num_friends):
            friends.append(friend)
        return friends

    def get_home_time_line(self,num_tweets):
        home_timeline_tweets=[]
        for tweet in Cursor(self.twitter_clent.home_timeline,id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return  home_timeline_tweets

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
        listener = TwitterListener(tweet_filename)
        auth=self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
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
        if status_code==420:
            #Returning false on data method in case limit occurs.
            return False
        print(status_code)

class TweetAnalyzer():
    #Analyze tweets
    def tweets_to_dataframe(self,tweets):
        df=pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['Tweets'])

        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['id'] = np.array([tweet.id for tweet in tweets])
        df['Date'] = np.array([tweet.created_at for tweet in tweets])
        df['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['Retweet'] = np.array([tweet.retweet_count for tweet in tweets])
        df['Device'] = np.array([tweet.source for tweet in tweets])
        return df

if __name__=='__main__':
    twitter_client=TwitterClient()
    tweet_analyzer=TweetAnalyzer()

    api=twitter_client.get_twitter_client_api()
    tweets=api.user_timeline(screen_name="realDonaldTrump",count=20)
    #print(dir(tweets[0]))

    df=tweet_analyzer.tweets_to_dataframe(tweets)

    # print(df.head(10))
    # print(tweets[0].id)
    # print("Retweeted:",tweets[0].retweet_count,"times")
    # print(df.head(10))
    html=df.to_html("index")
    print(df)
    # hashtag_list=['donald trump','barack obama']
    # tweet_filename="tweets.json"
    #
    # twitter_client=TwitterClient('balaton sound')
    # print(twitter_client.get_user_timeline_tweets(1))
    # twitter_streamer=TwitterStreamer()
    # twitter_streamer.stream_tweets(tweet_filename,hashtag_list)
