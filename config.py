import os
from dotenv import load_dotenv
load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_VIDEO_ID = os.getenv("YOUTUBE_VIDEO_ID")
INSTAGRAM_APIFY_TOKEN = os.getenv("INSTAGRAM_APIFY_TOKEN")