import pandas as pd
from fetchers.restcountries_fetcher import fetch_country_data
from fetchers.twitterapiio_fetcher import fetch_twitter_replies
from fetchers.instagram_fetcher import fetch_instagram_comments
from fetchers.youtube_fetcher import fetch_youtube_comments
from fetchers.trends_fetcher import fetch_trends
from utils import combine_sources, save_json

def run():
    country = fetch_country_data("indonesia")
    trends = fetch_trends("ekonomi indonesia")

    tweet_id = "1199995403002732545"
    tweets = fetch_twitter_replies(tweet_id, max_items=400)
    insta = fetch_instagram_comments(max_items=400)
    youtube = fetch_youtube_comments(max_items=400)

    save_json(tweets, "tweets.json")
    save_json(insta, "instagram.json")
    save_json(youtube, "youtube.json")

    texts = combine_sources({
        "twitter": tweets,
        "instagram": insta,
        "youtube": youtube,
    })

    save_json(country, "country.json")
    trends.to_csv("trends.csv", index=False)
    save_json(texts, "opinion_of_all_texts.json")

if __name__ == "__main__":
    run()