import snscrape.modules.twitter as sntwitter
import pandas as pd
query = "Uk"
#query = "from:anyasorchigozie since:2023-01-01 until:2023-05-31"
#query = "from:sterlinghelp"
tweets =[]
limits = 50

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.user.displayname, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Display Name','Tweet'])
df.to_csv("aaa.csv")
print(df)