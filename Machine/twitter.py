# %%
import snscrape.modules.twitter as sntwitter
import pandas as pd 
from time import *
import psycopg2

# %%
class Tweet_list():

    def tweets_list1(self):

        dbname = 'machine'
        user = 'postgres'
        password = 'AngelM09'
        host = 'localhost' 
        port = 5432
        cur = None
        conn = None
        
        try:
            conn = psycopg2.connect(
                    dbname = dbname,
                    user = user,
                    password = password,
                    host = host, 
                    port = port   
            )

            cur = conn.cursor()

            cur.execute('DROP TABLE IF EXISTS Machine_twitter')

            create_table =  '''CREATE TABLE IF NOT EXISTS Machine_twitter (
                id      serial PRIMARY KEY,
                Tweet   text,
                Tweet_id    BIGINT,
                Timestamp   timestamp,
                Replys   int,
                Retweets    int,
                Likes   int,
                Username    VARCHAR)''' 

            cur.execute(create_table)

            for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:TheHoopCentral').get_items()):
                if i > 5:
                    break
                insert_tweet = 'INSERT INTO Machine_twitter (Tweet, Tweet_id, Timestamp, Replys, Retweets, Likes, Username) VALUES (%s, %s, %s, %s,%s, %s, %s)'
                insert_values = (tweet.content, tweet.id, tweet.date, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.user.username)
                cur.execute(insert_tweet, insert_values)
                
            conn.commit()
            print('completed')

        except Exception as error:
                print(error)  

        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


# %%
tweets = Tweet_list()
tweets2 = Tweet_list()

tweets2.tweets_list1()


