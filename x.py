import tweepy
import time
import random

# مفاتيح الدخول الجديدة
bearer_token = 'AAAAAAAAAAAAAAAAAAAAANLz3QEAAAAABCzPeKvNlLXd59bW6QIJ1gQYoHA%3D3bZIPSHSXDv6PDq1YBvBb2FOybJenDHVzhOPXjkjaBpMNQmQRF'
consumer_key = 'd05yyViWnWrDDLZ6OOnOw1uO0'
consumer_secret = 'OSa55A2vjQY4jFV1auWjWjomarVQIoOpS0G0eRnpykL5Yhjwmo'
access_token = '262755582-vTMuj7msspVfxzHsiMFbXVEjOR1lLDkQkzTXZ2NI'
access_token_secret = 'fJnyqbkYGzHrjO36A0cWQgxjIPzB2GlWvhClyV1V2ZJuL'

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def get_duas():
    with open('duas.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def generate_unique_suffix():
    symbols = ['.', '*', '+', '^', '#', '~', '•', ':']
    number = random.randint(1, 999)
    symbol = random.choice(symbols)
    return f" {symbol}{number}"

if __name__ == "__main__":
    duas = get_duas()
    while True:
        dua = random.choice(duas)
        tweet = dua + generate_unique_suffix()
        try:
            response = client.create_tweet(text=tweet)
            print(f"تم التغريد: {tweet}")
        except Exception as e:
            print(f"خطأ في التغريد: {e}")
        time.sleep(86400)
