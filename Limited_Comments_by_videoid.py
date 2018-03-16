from apiclient.discovery import build
import pandas as pd
import time

DEVELOPER_KEY = "AIzaSyCyODQsYeGLjRzbT3K5N8JEIJG6EMiWTnQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


def get_comment_threads2(youtube, video_id):
  results = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText"

  ).execute()

  for item in results["items"]:
    comment = item["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print ("Comment by %s: %s" % (author, text))


  return results["items"]