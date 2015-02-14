import tweepy
import time
#Authenticates twitter API
auth = tweepy.OAuthHandler('V4kncK07KHZ2V9RRePa7myQ7l', '2dxr53rpTtpCNM1yUqE0ofQxg0wZC2lZy66FHow89MERTaQjTO')
auth.set_access_token('838703438-7fD9TxqICgCWsZi35MGjve60J15u9ViTWIdIbEZe', 'qwLmo3FaQU1JN0sBqqqE1pNsylNYPaTs5weXzU6PiRj4U')

api = tweepy.API(auth)
user = api.get_user("ritmish")
print user.screen_name
followers = []
for friend in user.followers():
	followers.append(friend.screen_name)
	
ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="xkcd").pages():
    ids.extend(page)
    time.sleep(1)
    
screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]
print screen_names
