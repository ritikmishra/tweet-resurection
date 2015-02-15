import tweepy
import time
import random
import guidata
import guidata.dataset.datatypes as dt
import guidata.dataset.dataitems as di

    
from sys import exit
ids = []
last_tweet = 0
def get_statuses():
	global ids, api, creepee, last_tweet, output
	previous_ids = []
	ids = []
	
	
	for status in api.user_timeline(creepee,count=200, page=2):
		ids.append(status.id)
		last_tweet = ids[len(ids)-1]
		appended_content = unicode(status.author.screen_name + " said \"" + status.text + "\" \n")
		output.write(appended_content.encode('ascii', 'ignore'))
		

	
	
class Processing(dt.DataSet):
    """Example"""
    
    b = di.StringItem("Username", default="App will return most recent 200 tweets from this person")
    c = di.ButtonItem("Test", get_statuses)


def main(app_set):
	global ids, api, creepee, last_tweet, output
	try:
		consumer_key=["HIDDEN"]
		consumer_secret=["Hidden"]
		access_token=["HIDDEN"]
		access_secret=["Hiddens"]
		app_set = app_set
		#Authenticates twitter API
		auth = tweepy.OAuthHandler(consumer_key[app_set], consumer_secret[app_set])
		#Joseph said he hates OAuth
		auth.set_access_token(access_token[app_set], access_secret[app_set])
		api = tweepy.API(auth)
		username = raw_input(str("Enter a Twitter handle to get its followers: "))
		
		if username[0] == '@':
			username = username[1:]
		user = api.get_user(username)
		
		
		
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
			creepee = creepee[1:]
		output = open(creepee + '.txt', 'a')
		get_statuses()
	except tweepy.error.TweepError:
		last_tweet = ids[len(ids)-1]
		api.retweet(last_tweet)
		exit("Crashed with an error.")
	except IndexError:
		print("This user doesn't have 200 tweets, the minimum required to automatically creep.")		
	finally:
		print("Exiting...")
main(0)
		
