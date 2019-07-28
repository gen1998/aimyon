import tweepy

CONSUMER_KEY = "pdjDSvfOjBQorPtjfdcTrdmol"
CONSUMER_SECRET = "oyl3mx4c8hrio2Vuz71g4Vq2vnBnIKBweFEYxCP5G2Qjh6VAZl"
ACCESS_TOKEN = "1142086183771504642-LWlh3rc3sMLw3n7KabfqzUzpv1o4sT"
ACCESS_TOKEN_SECRET = "GtSeMpsoKkcWlyXhTp7jCSP2DZCYwCgoclE65HNn0CKKA"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)
followers_ids = tweepy.Cursor(api.followers_ids, id='eren_word_maker', cursor=-1).items()
for follower_id in followers_ids:
    try:
        user = api.get_user(follower_id)
        api.create_friendship(user.screen_name)
        print(user.screen_name)
    except tweepy.error.TweepError as e:
        print(e.reason)
