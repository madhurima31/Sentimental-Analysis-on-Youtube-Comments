from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyCyODQsYeGLjRzbT3K5N8JEIJG6EMiWTnQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_comments(video_id, channel_id):
 youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

 search_response = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    channelId=channel_id,
    textFormat="plainText"
  ).execute()

 for item in search_response["items"]:
    comment = item["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print("Comment by %s: %s" % (author, text))

 return search_response["items"]

video_comments = get_comments( "XRkaVrhDE4U", "UCZBmZvV5MqQT4XbZ-wSnSAA")



# def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):
#
#   youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
#     developerKey=DEVELOPER_KEY)
#
#   search_response = youtube.search().list(
#     q=q,
#     type="video",
#     pageToken=token,
#     order = order,
#     part="id,snippet",
#     maxResults=max_results,
#     location=location,
#     locationRadius=location_radius
#
#   ).execute()
#
#
#
#
#
#   videos = []
#
#   for search_result in search_response.get("items", []):
#     if search_result["id"]["kind"] == "youtube#video":
#       videos.append(search_result)
#   try:
#       nexttok = search_response["nextPageToken"]
#       return(nexttok, videos)
#   except Exception as e:
#       nexttok = "last_page"
#       return(nexttok, videos)