import os
import requests
import asyncio
import threading
import random
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

sqlalchemy = SQLAlchemy()
sqlalchemy.init_app(app)
db = SQLAlchemy(app)

DEVELOPER_KEY = 'AIzaSyDKYsF__QLc1WVvFkHR-oXThiuLz3dmtZ8'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


class Youtubedata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(120))
    thumbnail = db.Column(db.String(120))
    thumbnailm = db.Column(db.String(120))
    thumbnailh = db.Column(db.String(120))
    published_at = db.Column(db.String(80))
    channel_title = db.Column(db.String(80))

    def __init__(self, title, description, thumbnail, thumbnailm, thumbnailh, published_at, channel_title):
        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        self.thumbnailm = thumbnailm
        self.thumbnailh = thumbnailh
        self.published_at = published_at
        self.channel_title = channel_title

    def addthis(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<Youtube %r>' % self.title


def addtodatabase(dicttoparse):
    title = dicttoparse["title"]
    description = dicttoparse["description"]
    thumbnails = dicttoparse["thumbnails"]["default"]["url"]
    thumbnailsm = dicttoparse["thumbnails"]["medium"]["url"]
    thumbnailsh = dicttoparse["thumbnails"]["high"]["url"]
    channelTitle = dicttoparse["channelTitle"]
    publishedAt = dicttoparse["publishedAt"]

    Youtubedata(title=title, description=description, thumbnail=thumbnails, thumbnailm=thumbnailsm,
                thumbnailh=thumbnailsh, published_at=publishedAt, channel_title=channelTitle)


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part='id,snippet',
        maxResults=options.max_results
    ).execute()

    for eachvideo in search_response["items"][[]]:
        print(eachvideo["id"]["videoId"])

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            addtodatabase(search_result['snippet'])
            videos.append('%s (%s)' % (search_result['snippet']['title'],
                                       search_result['id']['videoId']))
        elif search_result['id']['kind'] == 'youtube#channel':
            channels.append('%s (%s)' % (search_result['snippet']['title'],
                                         search_result['id']['channelId']))
        elif search_result['id']['kind'] == 'youtube#playlist':
            playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                          search_result['id']['playlistId']))

    print('Videos:\n', '\n'.join(videos), '\n')
    print('Channels:\n', '\n'.join(channels), '\n')
    print('Playlists:\n', '\n'.join(playlists), '\n')


@app.route('/')
def index():
    youtubedata = Youtubedata.query.all()
    return render_template('index.html', youtubedata=youtubedata)


@app.route('/json', methods=['GET', 'POST'])
def takejson():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify(data)
    elif request.method == 'GET':
        return jsonify({'message': 'Hello World!'})

    else:
        return jsonify({'message': 'wrong method'})

    # GETTING REQUESTED DATA

    data = request.get_json()

    apiid = data["apiid"]
    apifw = data["apifw"]
    sourcev = data["sourcev"]
    apireq = data["apireq"]

    # APPLYING LOGIC

    # PREPARING RESPONSE

    response = {"downloadlink": "files/" + downloadlink}

    # Check if user sent a name at all
    if not apiid:
        response["ERROR"] = "please provide API ID"
    # Check if the user entered a number not a name
    elif not apifw:
        response["ERROR"] = "please provide API Framework"
    # Now the user entered a valid name
    else:

        response["MESSAGE"] = f"how you doin ???"

    # Return the response in json format
    print(response)

    return jsonify(response)


async def get_youtube():
    ytapikey = ["AIzaSyDKYsF__QLc1WVvFkHR-oXThiuLz3dmtZ8", "AIzaSyDKYsF__QLc1WVvFkHR-oXThiuLz3dmtZ8",
                "AIzaSyDzPcLPAjFUQwNkqscSKVnV56OS6eVHFwI", "AIzaSyCSVSuqDtRGL2ak-7zQkfeJiBU8qJhnoJM",
                "AIzaSyDgfH_OfNgkymD72IezkFPPyhMjXSKFG5g"]
    rankeynum = random.randint(1, len(ytapikey))
    youtube_key = ytapikey[rankeynum]
    youtube_url = "https://www.googleapis.com/youtube/v3/search"
    youtube_params = {
        "part": "snippet",
        "q": "python",
        "key": youtube_key,
        "maxResults": 10
    }
    while True:

        youtube_response = requests.get(youtube_url, params=youtube_params)
        youtube_data = youtube_response.json()
        try:
            for data in youtube_data["items"]:
                # Key to find if data is present or not.
                videoId = data["id"]
                videoTitle = data["snippet"]["title"]
                description = data["snippet"]["description"]
                publishedAt = data["snippet"]["publishedAt"]
                thumbnailUrl = data["snippet"]["thumbnails"]["medium"]["url"]
                channelName = data["snippet"]["channelTitle"]
                print(videoTitle)

                Youtubedata(title=videoTitle, description=description, thumbnail=thumbnailUrl, video_id=videoId,
                            published_at=publishedAt, channel_title=channelName).addthis()


        except Exception as e:
            print(e)

        await asyncio.sleep(10)


# Function for initialising Async Loop
def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(get_youtube())


# Puts the get request in background
loop = asyncio.get_event_loop()
t = threading.Thread(target=loop_in_thread, args=(loop,))
t.start()

db.create_all()
db.session.commit()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7000))
    app.run(threaded=True, port=port, debug=True)
