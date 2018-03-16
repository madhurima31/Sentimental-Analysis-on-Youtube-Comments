import sys

# sys.path.append("D:\data analytics and ML\Analytics\TrialYoutube2.py")
# sys.path.append("D:\data analytics and ML\Analytics\Comments_by_videoid.py")
# sys.path.append("D:\data analytics and ML\Analytics\Comments_by_Channel.py")

from Search_data_by_keyword import youtube_search
from Comments_by_Channel import get_videos_FromChanel, youtube , get_comment_threads
# from Comments_by_videoid import get_comment_threads2
# from All_Comments_by_videoid import YouTubeApi
from All_comments_into_csv import  YouTubeApi

import json
# test=youtube_search("panda")
# print(test)

# videos = get_videos_FromChanel(youtube, "UCuAHfJyWROB4XRReS43EWUw")

# comments_thread = get_comment_threads2(youtube,"dOUV2rwMr1g")
# print(comments_thread)

y= YouTubeApi()
t=y.get_video_comment()
print(t)