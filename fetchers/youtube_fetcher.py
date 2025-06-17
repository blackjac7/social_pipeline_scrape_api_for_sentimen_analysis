from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY, YOUTUBE_VIDEO_ID

def fetch_youtube_comments(max_items=400):
    yt = build("youtube","v3", developerKey=YOUTUBE_API_KEY)
    comments, token = [], None
    while len(comments) <= max_items:
        req = yt.commentThreads().list(
            part="snippet", videoId=YOUTUBE_VIDEO_ID, maxResults=400, pageToken=token
        )
        res = req.execute()
        for item in res.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            txt = snippet["textDisplay"]
            comment_id = item["snippet"]["topLevelComment"]["id"]
            published_at = snippet.get("publishedAt", "")
            comments.append({
                "id": comment_id,
                "text": txt,
                "source": "youtube",
                "timestamp": published_at
            })
        token = res.get("nextPageToken")
        if not token:
            break
    return comments[:max_items]