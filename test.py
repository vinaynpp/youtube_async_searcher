import requests
import random

ytapikey = [ "AIzaSyDKYsF__QLc1WVvFkHR-oXThiuLz3dmtZ8", "AIzaSyDKYsF__QLc1WVvFkHR-oXThiuLz3dmtZ8", "AIzaSyDzPcLPAjFUQwNkqscSKVnV56OS6eVHFwI", "AIzaSyCSVSuqDtRGL2ak-7zQkfeJiBU8qJhnoJM", "AIzaSyDgfH_OfNgkymD72IezkFPPyhMjXSKFG5g"]
rankeynum = random.randint(1,  len(ytapikey))
youtube_key = ytapikey[rankeynum]






youtube_url = "https://www.googleapis.com/youtube/v3/search"
youtube_params = {
    "part": "snippet",
    "q": " Keen Psyche",
    "key": youtube_key,
    "maxResults": 10
}

youtube_response = requests.get(youtube_url, params=youtube_params)
print(youtube_response)
youtube_data = youtube_response.json()
print(youtube_data)

for data in youtube_data["items"]:
    # Key to find if data is present or not.
#        key = {'videoId': data["id"]["videoId"]}
    videoId = data["id"]
    videoTitle = data["snippet"]["title"]
    description = data["snippet"]["description"]
    publishedAt = data["snippet"]["publishedAt"]
    thumbnailUrl = data["snippet"]["thumbnails"]["medium"]["url"]
    channelName = data["snippet"]["channelTitle"]
    print(description)
        
#        Youtubedata(title=videoTitle, description=description, thumbnail=thumbnailUrl, video_id=videoId, published_at=publishedAt, channel_title=channelName).addthis()


