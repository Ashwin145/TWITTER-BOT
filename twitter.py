
import tweepy 

print('this is my twitter bot')
CONSUMER_KEY="CONSUMER_KEY TOKEN"
CONSUMER_SECRET = "CONSUMER_SECRET TOKEN "
ACCESS_KEY = "ACCESS_KEY TOKEN "
ACCESS_SECRET = "ACCESS_SECRET TOKEN"

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id)+ '- '+ mention.text)
