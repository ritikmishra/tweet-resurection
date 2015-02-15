import tweepy
import time
import random
import getpass
from sys import exit
ids = []
def get_statuses():
	global ids, api, creepee, last_tweet
	previous_ids = []
	ids = []
	
	for status in api.user_timeline(creepee,count=200, page=2):
		ids.append(status.id)
		print status.author
		print " said \"" + status.text + "\""
		last_tweet = ids[len(ids)-1]
	
	api.retweet(last_tweet)
	
def main(app_set):
	global ids, api, creepee, last_tweet
	try:
		consumer_key=["V4kncK07KHZ2V9RRePa7myQ7l", "Du6zndJP8C5ZqIozpPyIWMMIy"]
		consumer_secret=['HIDDEN']
		access_token=["838703438-7fD9TxqICgCWsZi35MGjve60J15u9ViTWIdIbEZe", "838703438-4IZl6z7SAj7DE2NcSD8nyNgsKz4cexpMc0I8djPK"]
		access_secret=['HIDDEN']
		app_set = app_set
		#Authenticates twitter API
		auth = tweepy.OAuthHandler(consumer_key[app_set], consumer_secret[app_set])
		#Joseph said he hates OAuth
		auth.set_access_token(access_token[app_set], access_secret[app_set])
		api = tweepy.API(auth)
		username = raw_input(str("Twitter Handle: "))
		password = getpass.getpass("Twitter Password: ")
		
		if username[0] == '@':
			username = username[1:]
		user = api.get_user(username)
		
		print "Logged in as " + user.screen_name
		
		followers = []
		ids = []
		
		for friend in user.followers():
			if not friend.protected:
				followers.append(friend.screen_name)
		
		for x in followers:
			print x
		
		follower_numbers = range(len(followers))
		creepee = str(raw_input("Above are your Creep-able followers. Enter a Twitter handle to resurect an old tweet."))
		if creepee[0] == '@':
			creepee = crepee[1:]
		get_statuses()
	except tweepy.error.TweepError:
		last_tweet = ids[len(ids)-1]
		api.retweet(last_tweet)
		exit("Crashed with an error.")
		
	finally:
		print("Exiting...")
main(0)
		
