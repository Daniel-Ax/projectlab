import sys
import tweepy
import tkinter as tk

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
#ISTHISc

win=tk.Tk()
win.title("Get news")
win.mainloop()