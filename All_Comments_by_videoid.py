from apiclient.discovery import build
import pandas as pd
import json
import time


import argparse
from urllib.parse import urlparse, urlencode, parse_qs
from urllib.request import  urlopen




YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'



class YouTubeApi():

    def get_video_comment(self):

        def load_comments(self):
            for item in mat["items"]:
                comment = item["snippet"]["topLevelComment"]
                author = comment["snippet"]["authorDisplayName"]
                text = comment["snippet"]["textDisplay"]
                print("Comment by {}: {}".format(author, text))
                print(item)


        mxRes = 20
        vid = str()



        parms = {
                    'part': 'snippet,replies',
                    'maxResults': 50,
                    # 'videoId': "dOUV2rwMr1g",
                    'videoId': "_JCSGQWGsr4",

                    'textFormat': 'plainText',
                    'key': "AIzaSyCyODQsYeGLjRzbT3K5N8JEIJG6EMiWTnQ"
                }

        try:

            matches = self.openURL(YOUTUBE_COMMENT_URL, parms)
            i = 2
            mat = json.loads(matches)
            nextPageToken = mat.get("nextPageToken")
            print("\nPage : 1")
            print("------------|||||||||||||||----------------------")
            load_comments(self)

            while nextPageToken:
                parms.update({'pageToken': nextPageToken})
                matches = self.openURL(YOUTUBE_COMMENT_URL, parms)
                mat = json.loads(matches)
                nextPageToken = mat.get("nextPageToken")
                print("\nPage : ", i)
                print("------------||||||||||||||||-------------------")

                load_comments(self)

                i += 1

        except:
            print("Cannot Open URL or Fetch comments at a moment")

        return mat["items"]



    def openURL(self, url, parms):
              f = urlopen(url + '?' + urlencode(parms))
              data = f.read()
              f.close()
              matches = data.decode("utf-8")
              return matches

