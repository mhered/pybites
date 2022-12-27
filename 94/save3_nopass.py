from collections import namedtuple
import os
import pickle
import urllib.request
import re
from datetime import timedelta


# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = f'https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}'
tmp = os.getenv("TMP", "/tmp")
pycon_videos = os.path.join(tmp, pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

from pprint import pprint

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    with open(pycon_videos, 'rb') as f:
        return pickle.load(f)


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    return sorted(videos, key=lambda x:int(x.metrics['viewCount']),reverse=True)    


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
       
    fun = lambda x: (int(x.metrics['likeCount']) - int(x.metrics['dislikeCount']))/ int(x.metrics['viewCount'])
    return sorted(videos, key=fun,reverse=True)    


def _video_duration(duration_str):
    
    hours=int(re.search('[0-9]+(?=H)', duration_str).group(0)) if 'H' in duration_str else 0
    minutes=int(re.search('[0-9]+(?=M)', duration_str).group(0)) if 'M' in duration_str else 0
    seconds=int(re.search('[0-9]+(?=S)', duration_str).group(0)) if 'S' in duration_str else 0
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return [video for video in videos if _video_duration(video.duration) > timedelta(hours=1)] 


def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    return [video for video in videos if _video_duration(video) < timedelta(minutes=24)] 


if __name__ =='__main__':
    top=10
    videos = load_pycon_data()
    print(" ".join([item.metrics['viewCount'] for item in videos[0:top] ]))
    popular_videos = get_most_popular_talks_by_views(videos)
    print(" ".join([item.metrics['viewCount'] for item in popular_videos[0:top]]))
    
    liked_videos = get_most_popular_talks_by_like_ratio(videos)
    print(" ".join([
                    str(
                        100*((int(item.metrics['likeCount'])-int(item.metrics['dislikeCount'])) / 
                        int(item.metrics['viewCount']))) for item in liked_videos[0:top]]
                )
        )

    print(_video_duration('PT3H17M9S'))