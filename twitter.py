
import tweepy 

print('this is my twitter bot')
CONSUMER_KEY=" weiqsoXkRXvakgfE9XsE8JuFE"
CONSUMER_SECRET = "iWRyuB005f9iXsoOuAAO51biCXnN7xhy0iiOskOEjrTtNVejJ1 "
ACCESS_KEY = "1486293949925175303-uZLIQakOslWRKiS6A2miLI6H4SYitb "
ACCESS_SECRET = " 6lGvy9VLdno86A3S5jGEmAll8wCUjBFwpsIhg8Wi1qCGn"

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id)+ '- '+ mention.text)