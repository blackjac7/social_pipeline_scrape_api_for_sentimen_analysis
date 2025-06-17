import requests
from config import TWITTER_API_KEY

def fetch_twitter_replies(tweet_id: str, max_items: int = 400):
    url = "https://api.twitterapi.io/twitter/tweet/replies"
    headers = {
        "X-API-Key": TWITTER_API_KEY
    }
    params = {
        "tweetId": tweet_id,
    }

    replies = []
    cursor = ""
    while len(replies) <= max_items:
        if cursor:
            params["cursor"] = cursor

        resp = requests.get(url, headers=headers, params=params)
        try:
            resp.raise_for_status()
        except Exception as e:
            print(f"Error fetching replies: {e}")
            break

        data = resp.json()
        if data.get("status") != "success":
            print(f"API error: {data.get('message', 'Unknown error')}")
            break

        for item in data.get("tweets", []):
            replies.append({
                "id": item.get("id"),
                "text": item.get("text", ""),
                "timestamp": item.get("createdAt"),
                "source": "twitter"
            })
            if len(replies) >= max_items:
                break

        if not data.get("has_next_page") or not data.get("next_cursor"):
            break
        cursor = data.get("next_cursor")

    return replies[:max_items]