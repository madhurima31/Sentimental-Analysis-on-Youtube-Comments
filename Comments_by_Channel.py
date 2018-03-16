from apiclient.discovery import build
import pandas as pd
import time

DEVELOPER_KEY = "AIzaSyCyODQsYeGLjRzbT3K5N8JEIJG6EMiWTnQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


def get_videos_FromChanel(youtube, channelId):
    search_response = youtube.search().list(
        channelId=channelId,

        type="video",
        part="id,snippet",
        maxResults=50,

    ).execute()

    return search_response.get("items", [])


def get_comment_threads(youtube, videos):
    tempComments = []
    for video in videos:
        time.sleep(1.0)
        print( video["snippet"]["title"])
        video["snippet"]["title"]
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=video["id"]["videoId"],
            textFormat="plainText",
            maxResults=20,
            order='relevance'
        ).execute()

        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]
            tempComment = dict(videoId=video["id"]["videoId"], videoName=video["snippet"]["title"],
                               nbrReplies=item["snippet"]["totalReplyCount"],
                               author=comment["snippet"]["authorDisplayName"], likes=comment["snippet"]["likeCount"],
                               publishedAt=comment["snippet"]["publishedAt"],
                               text=comment["snippet"]["textDisplay"].encode('utf-8').strip())
            tempComments.append(tempComment)

    return tempComments


# def get_comment_threads2(youtube, video_id):
#   results = youtube.commentThreads().list(
#     part="snippet",
#     videoId=video_id,
#     textFormat="plainText"
#   ).execute()
#
#   for item in results["items"]:
#     comment = item["snippet"]["topLevelComment"]
#     author = comment["snippet"]["authorDisplayName"]
#     text = comment["snippet"]["textDisplay"]
#    # print ("Comment by %s: %s" % (author, text))
#
#   # return results["items"]
#   return results["items"]