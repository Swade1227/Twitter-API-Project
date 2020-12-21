import tweepy

auth = tweepy.OAuthHandler("raMYtMBZdSiWoAKRJA8tc3kk2", "c7N20Ayf7LC2Wq1yRA4OQCRFYKbnUVCeExJmTYzleoZHbiRjzb")
auth.set_access_token("1340379552753848321-RSaDYOYR8QNhlGEoSGkXtgKL98v2Wo", "KvMwQ41IDaDJxSU5gSN5wOXXAuDd8Mfgbat1J6sHgv5OG")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)