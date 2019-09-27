'''
Extracting Images from the Twitter Streaming API
Based on the tutorials from: https://pythonprogramming.net/data-analysis-tutorials/
'''

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import env
import wget


ckey=env.apiKey
csecret=env.apiSecret
atoken=env.accessToken
asecret=env.accessSecret

dl_path = env.path

class listener(StreamListener):
    def on_data(self, data, include_entities=True, tweet_mode="extended"):
        all_data = json.loads(data)

        for item in all_data["entities"]:
            if item == "media":
                try:
                    # Dowloading the image urls
                    media_file = all_data["extended_entities"]["media"][0]["media_url_https"]
                    print(media_file)
                    wget.download(media_file, dl_path)

                except KeyError:
                    pass



    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["flowers"])

