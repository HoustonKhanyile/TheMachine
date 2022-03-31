import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list1 = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:ShannonSharpe').get_items()):
    if i > 10:
        break
    tweets_list1.append([tweet.content, tweet.id, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.user.username])

tweets_df1 = pd.DataFrame(tweets_list1, columns=['Text', 'Tweet id', 'likeCount', 'retweetCount', 'replyCount', 'Username'])
print(tweets_df1)
