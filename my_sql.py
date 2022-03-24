import mysql.connector
from stop_word import *

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "admin",
    database = "tweety"
)
mycursor = mydb.cursor()

def add_items(item):
    
    for tweet in item:
        tweet_text = str(tweet.full_text)
        
        if 'RT' in tweet_text:
            text = clear_words(str(tweet.retweeted_status.full_text))
           
            val = (str(tweet.retweeted_status.id),str(tweet.retweeted_status.user.screen_name),str(text),str(tweet.retweeted_status.user.location))
            
        else:
            text = clear_words(str(tweet.full_text))
            # print(text)
            # try:
            val = (str(tweet.id),str(tweet.user.screen_name),str(text),str(tweet.user.location))
            
        # print(val)
        
        add_query = "INSERT INTO tdata VALUES (%s,%s,%s,%s,null,null)"
        mycursor.execute(add_query,val)
    
    mydb.commit()
    
    # print("commit")
