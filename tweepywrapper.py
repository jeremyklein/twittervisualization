import tweepy
import json


class TweepyWrapper:
	def __init__(self):
		with open("../credentials.json") as f:
			jsonCred = f.read()
		credentials = json.loads(jsonCred)
		consumer_key =credentials['twitter']['consumer_key']
		consumer_secret =credentials['twitter']['consumer_secret']
		access_token = credentials['twitter']['access_token']
		access_token_secret = credentials['twitter']['access_token_secret']
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		self.api = tweepy.API(auth)

	def search(self, search_term):
		searched_tweets = [status for status in tweepy.Cursor(self.api.search, q=search_term).items(100)]
		return searched_tweets

	def getLocations(self, searched_tweets):
		for tweet in searched_tweets:
			if (tweet.geo != None):
				print tweet.geo

if __name__=='__main__':
	tweetwrapper = TweepyWrapper()
	searched_tweets = tweetwrapper.search("#trump")
	tweetwrapper.getLocations(searched_tweets)
	print json.dump(searched_tweets)