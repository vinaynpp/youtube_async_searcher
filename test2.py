import json


def addtodatabase(dicttoparse):

    title = dicttoparse["title"]
    description = dicttoparse["description"]
    thumbnails = dicttoparse["thumbnails"]["default"]["url"]
    thumbnailsm = dicttoparse["thumbnails"]["medium"]["url"]
    thumbnailsh = dicttoparse["thumbnails"]["high"]["url"]
    channelTitle = dicttoparse["channelTitle"]
    publishedAt = dicttoparse["publishedAt"]



    print(dicttoparse["title"])
    print(dicttoparse["description"])
    print(dicttoparse["thumbnails"]["default"]["url"])
    print(dicttoparse["thumbnails"]["medium"]["url"])
    print(dicttoparse["thumbnails"]["high"]["url"])
    print(dicttoparse["channelTitle"])
    print(dicttoparse["publishedAt"])
    print(dicttoparse["publishedAt"][:10])
    print(dicttoparse["publishedAt"][11:19])


dicti = {'kind': 'youtube#searchListResponse', 'etag': 'NBz-B3c-JZ1j27KUiyj2NE_MU_c', 'nextPageToken': 'CAoQAA',
         'regionCode': 'IN', 'pageInfo': {'totalResults': 1000000, 'resultsPerPage': 10}, 'items': [
        {'kind': 'youtube#searchResult', 'etag': '63vwa9SK07khzxC3527csktykhI',
         'id': {'kind': 'youtube#video', 'videoId': 'WNarpiGz3Kk'},
         'snippet': {'publishedAt': '2021-10-19T18:00:01Z', 'channelId': 'UCIG1k8umaCIIrujZPzZPIMA',
                     'title': 'Google Presents: Pixel Fall Launch',
                     'description': 'On October 19, we officially introduced Pixel 6 and Pixel 6 Pro—our completely reimagined phones. Powered by Google Tensor, ...',
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/WNarpiGz3Kk/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/WNarpiGz3Kk/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/WNarpiGz3Kk/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': 'Made by Google',
                     'liveBroadcastContent': 'none', 'publishTime': '2021-10-19T18:00:01Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'y3rnMR3sJuBW-3TulqCULstg87A',
         'id': {'kind': 'youtube#video', 'videoId': 'Z-pT0XDYvDM'},
         'snippet': {'publishedAt': '2020-11-18T23:01:52Z', 'channelId': 'UCHAK6CyegY22Zj2GWrcaIxg',
                     'title': 'Inside Google&#39;s Massive Headquarters',
                     'description': "We all use its services every day, it answers our most bizarre questions, you're even watching this video using the company's ...",
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/Z-pT0XDYvDM/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/Z-pT0XDYvDM/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/Z-pT0XDYvDM/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': 'Tech Vision',
                     'liveBroadcastContent': 'none', 'publishTime': '2020-11-18T23:01:52Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'xaSsxBkRR86P-cHXViA7HasRwFk',
         'id': {'kind': 'youtube#video', 'videoId': '-EjsCBHEbbk'},
         'snippet': {'publishedAt': '2020-11-28T09:58:28Z', 'channelId': 'UCJFWv8mN61O2b751dbwZXlw',
                     'title': 'ZOMBIE GIRL ESCAPE PREGNANCY PRANK BATTLE - Doctor Nerf Guns Couple Zombies Crime | Sky Nerf War',
                     'description': 'ZOMBIE GIRL ESCAPE PREGNANCY PRANK BATTLE - Doctor Nerf Guns Couple Zombies Crime | Sky Nerf War: ...',
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/-EjsCBHEbbk/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/-EjsCBHEbbk/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/-EjsCBHEbbk/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': 'Sky Nerf War',
                     'liveBroadcastContent': 'none', 'publishTime': '2020-11-28T09:58:28Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'IWwSLxEiaTcabk4PvKWm5cDsYQE',
         'id': {'kind': 'youtube#video', 'videoId': 'PTqtr3VSD5Q'},
         'snippet': {'publishedAt': '2021-04-13T01:11:17Z', 'channelId': 'UC5hU1TAA_DsdbCasVSNmIBg',
                     'title': 'TRY TO NOT LAUGH CHALLENGE. MUST WATCH NEW COMEDY VIDEOS 2021.Non Stop fun. Episode 113',
                     'description': 'TRY TO NOT LAUGH CHALLENGE. MUST WATCH NEW COMEDY VIDEOS 2021.Non Stop fun. If We have any mistake. please ...',
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/PTqtr3VSD5Q/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/PTqtr3VSD5Q/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/PTqtr3VSD5Q/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': 'Mihir Nath BD',
                     'liveBroadcastContent': 'none', 'publishTime': '2021-04-13T01:11:17Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'dp0iQsGK-sAyAfNlK-2oLpD_M80',
         'id': {'kind': 'youtube#video', 'videoId': 'KSIVrFui5Hg'},
         'snippet': {'publishedAt': '2019-11-11T04:00:00Z', 'channelId': 'UCUMxxg0KvWiSWHUXRPpnKzw',
                     'title': 'व्लाद एक सुपरहीरो में बदल जाता है  बच्चों के लिए संकलन वीडियो',
                     'description': 'व्लाद अपनी मां और छोटे भाई निकिता की मदद करने के लिए सुपरहीरो बन जाता है। कृपया सदस्यता लें!',
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/KSIVrFui5Hg/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/KSIVrFui5Hg/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/KSIVrFui5Hg/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': 'व्लाद और निकिता',
                     'liveBroadcastContent': 'none', 'publishTime': '2019-11-11T04:00:00Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'Ai3KCPmmwIoljtobnOgYBrrEX0U',
         'id': {'kind': 'youtube#video', 'videoId': 'qmNVJ4ZWQY0'},
         'snippet': {'publishedAt': '2019-10-19T07:29:11Z', 'channelId': 'UCk8GzjMOrta8yxDcKfylJYw',
                     'title': 'Diana and Dad - Funny Stories for Kids',
                     'description': "Diana and Dad - favorite children's stories about new toys and pretend play. Diana's INSTAGRAM ...",
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/qmNVJ4ZWQY0/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/qmNVJ4ZWQY0/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/qmNVJ4ZWQY0/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': '✿ Kids Diana Show',
                     'liveBroadcastContent': 'none', 'publishTime': '2019-10-19T07:29:11Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'z3o7j5xCVtXVdb3rnR8jDQ7ZBWQ',
         'id': {'kind': 'youtube#video', 'videoId': 'P7IvYsQuZCc'},
         'snippet': {'publishedAt': '2020-06-25T09:02:40Z', 'channelId': 'UCQP8-36ps4XMwo0-QB3ySJQ',
                     'title': 'HORROR COOKING - MAKING SEA LAMPREY STEAK',
                     'description': 'Thank for watching:"HORROR COOKING - MAKING SEA LAMPREY STEAK" SUBSCRIBE ...',
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/P7IvYsQuZCc/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/P7IvYsQuZCc/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/P7IvYsQuZCc/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': 'Horror Cooking',
                     'liveBroadcastContent': 'none', 'publishTime': '2020-06-25T09:02:40Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'alCJNwneB4utCMQoS4XNsYwiOn4',
         'id': {'kind': 'youtube#video', 'videoId': 'IMCDispQSTI'},
         'snippet': {'publishedAt': '2020-09-17T08:30:00Z', 'channelId': 'UCSx_w4q5PkAOg9i45uMFHmA',
                     'title': 'GOOGLY - Blockbuster Hindi Dubbed Action Romantic Movie | Yash Movies Hindi Dubbed | South Movie',
                     'description': 'Presenting South (Sauth) Indian Movies Dubbed In Hindi Full HD (Hindi Dubbed Full Movie, South Movie Hindi Dubbed, South ...',
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/IMCDispQSTI/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/IMCDispQSTI/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/IMCDispQSTI/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': 'AD-WISE MEDIA ACTION MOVIEPLEX',
                     'liveBroadcastContent': 'none', 'publishTime': '2020-09-17T08:30:00Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'kvhjh856M0mAu7k36rgjcG8HuHQ',
         'id': {'kind': 'youtube#video', 'videoId': 'FzG4uDgje3M'},
         'snippet': {'publishedAt': '2018-04-05T19:51:33Z', 'channelId': 'UC4rasfm9J-X4jNl9SvXp8xA',
                     'title': 'El Chombo - Dame Tu Cosita feat. Cutty Ranks (Official Video) [Ultra Music]',
                     'description': 'Check out the new "Dame Tu Cosita"! https://youtu.be/FMN3AtsXqA0 El Chombo - Dame Tu Cosita feat. Cutty Ranks El Chombo ...',
                     'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/FzG4uDgje3M/default.jpg', 'width': 120,
                                                'height': 90},
                                    'medium': {'url': 'https://i.ytimg.com/vi/FzG4uDgje3M/mqdefault.jpg', 'width': 320,
                                               'height': 180},
                                    'high': {'url': 'https://i.ytimg.com/vi/FzG4uDgje3M/hqdefault.jpg', 'width': 480,
                                             'height': 360}}, 'channelTitle': 'Ultra Music',
                     'liveBroadcastContent': 'none', 'publishTime': '2018-04-05T19:51:33Z'}},
        {'kind': 'youtube#searchResult', 'etag': 'xckyR9e0IMcBzKx5T8YK27os0Lo',
         'id': {'kind': 'youtube#channel', 'channelId': 'UCK8sQmJBp8GCxrOtXWBpyEA'},
         'snippet': {'publishedAt': '2005-09-18T22:37:10Z', 'channelId': 'UCK8sQmJBp8GCxrOtXWBpyEA', 'title': 'Google',
                     'description': 'Experience the world of Google on our official YouTube channel. Watch videos about our products, technology, company ...',
                     'thumbnails': {'default': {
                         'url': 'https://yt3.ggpht.com/ytc/AKedOLQhCqLTkEGQeSzNuaSndU18yVP8hqtaW-zJ4-ylRlw=s88-c-k-c0xffffffff-no-rj-mo'},
                                    'medium': {
                                        'url': 'https://yt3.ggpht.com/ytc/AKedOLQhCqLTkEGQeSzNuaSndU18yVP8hqtaW-zJ4-ylRlw=s240-c-k-c0xffffffff-no-rj-mo'},
                                    'high': {
                                        'url': 'https://yt3.ggpht.com/ytc/AKedOLQhCqLTkEGQeSzNuaSndU18yVP8hqtaW-zJ4-ylRlw=s800-c-k-c0xffffffff-no-rj-mo'}},
                     'channelTitle': 'Google', 'liveBroadcastContent': 'upcoming',
                     'publishTime': '2005-09-18T22:37:10Z'}}]}

# for eachvideo in dicti["items"]:
#     print(eachvideo["id"]["videoId"])

videos = []
channels = []
playlists = []

# Add each result to the appropriate list, and then display the lists of
# matching videos, channels, and playlists.
for search_result in dicti.get('items', []):
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

# print(json.dumps(dicti))
