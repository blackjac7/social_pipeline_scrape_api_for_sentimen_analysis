from apify_client import ApifyClient
from config import INSTAGRAM_APIFY_TOKEN

def fetch_instagram_comments(max_items=400):
    client = ApifyClient(INSTAGRAM_APIFY_TOKEN)

    run_input = {
    "addParentData": False,
    "directUrls": [
        "https://www.instagram.com/p/B8L6SR4Dtgw/",
        "https://www.instagram.com/p/B8Tpu_SAfDe/",
        "https://www.instagram.com/p/BxjjtCfJJ2a/",
        "https://www.instagram.com/p/BzFmtCaDvtH/",
        "https://www.instagram.com/p/B-V6jKHhqHv/",
        "https://www.instagram.com/p/CE9CdeOJoH1/"
    ],
    "enhanceUserSearchWithFacebookPage": False,
    "isUserReelFeedURL": False,
    "isUserTaggedFeedURL": False,
    "resultsLimit": max_items,
    "resultsType": "comments",
    "searchLimit": 1,
    "searchType": "hashtag"
    }

    run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

    results = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        results.append({
            "id": item.get("id", ""),
            "text": item.get("text", ""),
            "source": "instagram",
            "timestamp": item.get("timestamp", ""),
        })
        if len(results) >= max_items:
            break
    return results