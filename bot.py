from itertools import count
from numpy import result_type
import tweepy as tw
from my_sql import *
from datetime import date



api_key = "NEFOtIxBu9Q9qJ6CMR8Ym41kk"
api_secret_key = "3jojOmcu7JNwRCYXeDgwu7tBtuJ6l5526uPbfYJKBFV8eXGvMv"
access_token = "2587246627-Bdg7bjYHfLV3mzIBNDAasRID4Wz7EAmweYvpXbk"
access_token_secret = "XiTTDsRoGC30B9UQzHwwvLt9eMi0dJjv9PS8ZNtpDA3pT"

auth = tw.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tw.API(auth,wait_on_rate_limit=True)

search_word = {"Russia","Ukraine",'#RussiaUkrainCrisis','War','dead','Weapon','UkraineRussiaWar','Putin','Zelensky','Zelenskyy','#RussiaUkraine','#StandWithUkrain','#Kyiv','Kyiv'}
date_since = date.today

for a in search_word:
  tweets = tw.Cursor(api.search_tweets,q=a,lang="en",tweet_mode='extended',until = '2022-03-21').items()
  add_items(tweets)

  # print(str(tweet.place.country) + "\n" + str(tweet.user.screen_name) + "\n\n")
  # print(tweet.retweeted_status.full_text + "\n")
# for a in tweets:
#   print(a.text)


# new_status = api.update_status("Bot")

# public_tweets = api.home_timeline()

# word_used = ['Ukraine', 'Russia' , '#RussiaUkrainCrisis','War','war','shooting','dead','offensive']

# tweet_ids = [1,2]


#print(tokenize_words)
# while True:
#   public_tweets = api.home_timeline()
#   for a in public_tweets:
#     print(a.text+"\n")
#   time.sleep(2)
  
  #  return api

#twitter_auth()
