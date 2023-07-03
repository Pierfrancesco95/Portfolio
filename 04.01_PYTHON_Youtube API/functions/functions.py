import pandas as pd
import numpy as np

# for more details about below functions please see the following guide as reference (https://developers.google.com/youtube/v3/docs?hl=en)

# 1st function

def get_channel_stats(youtube, channel_ids):
    """
    Get channel statistics for a list of channels 
    
    Params
    ----------
    youtube: 
        the build object from googleapiclient.discovery

    channels_ids: list
        list of channel IDs
    
    Returns
    ----------
    Dataframe 
        containing the channel statistics for all channels in the provided list: title, date, country, subscriber count, view count, video count, upload playlist
    
    """
    all_data = []
    
    request = youtube.channels().list(
                                        part='snippet,contentDetails,statistics',
                                         id=','.join(channel_ids))
    response = request.execute() 
    
    for i in range(len(response['items'])):
        data = dict(channelName = response['items'][i]['snippet']['title'],                                    # The title of the channel
                    createdAt = response['items'][i]['snippet']['publishedAt'],                                # The date and time the channel was created
                    subscribers = response['items'][i]['statistics']['subscriberCount'],                       # The number of channel subscribers
                    views = response['items'][i]['statistics']['viewCount'],                                   # The number of times the channel has been viewed
                    totalVideos = response['items'][i]['statistics']['videoCount'],                            # The number of public videos uploaded to the channel
                    playlistId = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])        # The ID of the playlist that contains the videos uploaded by the channel
        all_data.append(data)
    
    return pd.DataFrame(all_data)



# 2nd function

def get_video_ids(youtube, playlist_id):
    """
    Get list of video IDs of all videos in the given playlist
    
    Params
    ----------
    youtube: 
        the build object from googleapiclient.discovery
    
    playlist_id: str
        playlist ID of the channel
    
    Returns
    ----------
    List
        List of video IDs of all videos in the given playlist
    
    """
    
    video_ids = []

    request = youtube.playlistItems().list(
                                            part='contentDetails',
                                            playlistId = playlist_id,
                                            maxResults = 50)
    response = request.execute()
    
    # get all videoIDs of the first page
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])

    # get all videoIDs of all the pages after the first one  

    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                                                    part='contentDetails',
                                                    playlistId = playlist_id,
                                                    maxResults = 50,
                                                    pageToken = next_page_token)
            response = request.execute()
    
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')
        
    return video_ids



# 3rd function

def get_video_details(youtube, video_ids):
    """
    Get a dataframe with all videos statistics of a given video IDs list

    Params
    ----------
    youtube: 
        the build object from googleapiclient.discovery

    video_ids: list
        list of video IDs
    
    Returns
    ----------
    Dataframe 
        with all videos statistics of a given video IDs list, i.e.: 
                                                                    'channelTitle',         # The title of the channel to which the video belongs
                                                                    'title',                # The title of the video
                                                                    'description',          # The description of the video
                                                                    'tags',                 # A list of keyword tags associated with the video
                                                                    'publishedAt',          # The date and time the video was posted
                                                                    'viewCount',            # The number of times the video has been viewed
                                                                    'likeCount',            # The number of users who indicated that they liked the video
                                                                    'commentCount',         # The number of comments for the video
                                                                    'duration',             # The duration of the video
                                                                    'definition',           # Indicates whether the video is available in high definition (HD) or standard definition only (SD)
                                                                    'caption'               # Indicates whether subtitles are available for the video (True) or not (False)
    """
        
    all_video_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
                                        part="snippet,contentDetails,statistics",
                                        id=','.join(video_ids[i:i+50])
        )
        response = request.execute() 


        for video in response['items']:
            stats_to_keep = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'statistics': ['viewCount', 'likeCount', 'commentCount'],
                             'contentDetails': ['duration', 'definition', 'caption']
                            }
            video_info = {}                             # for each video make a dictionary 
            video_info['video_id'] = video['id']        # assign the video_id string  to value of the key 'video_id' in the dictionary 'video_info'

            # make a key in the dictonary 'video_info' for each value in the dictionary 'stats_to_keep'
            # for each key of the dictonary 'video_info', get data from JSON 'response['items'][video][stats_to_keep.key][stats_to_keep.value]' and assign it to the value in the dictonary 'video_info'
            # append the dictionary 'video_info' to the list 'all_video_info'
            
            for k in stats_to_keep.keys():
                for v in stats_to_keep[k]:
                    try:
                        video_info[v] = video[k][v]    # i.e. video_info['channelTitle'] = response['items']['snippet']['channelTitle']
                    except:
                        video_info[v] = None

            all_video_info.append(video_info)  # make a list of dictionary (all with the same keys)
        
            
    return pd.DataFrame(all_video_info) # return a df with the list of dictionary


# 4th function

def get_comments_in_videos(youtube, video_ids):
    """
    Get top level comments as text from all videos with given IDs (only the first 10 comments due to quote limit of Youtube API)
    
    Params:
    ----------
    youtube: 
        the build object from googleapiclient.discovery
    
    video_ids: list
        list of video IDs
    
    Returns
    ----------
    Dataframe 
        with video IDs and associated top level comment in text.
    
    """
    all_comments = []
    
    for video_id in video_ids:
        try:   
            request = youtube.commentThreads().list(
                                                    part="snippet,replies",
                                                    videoId=video_id
            )
            response = request.execute()
        
            # with ['topLevelComment'] we take the first comment, after it we take the next 9 comments
            comments_in_video = [comment['snippet']['topLevelComment']['snippet']['textOriginal'] for comment in response['items'][0:10]]

            # make a dictionary for each row (video_id), assign a list of 10 comments
            comments_in_video_info = {'video_id': video_id, 'comments': comments_in_video}

            all_comments.append(comments_in_video_info) # make a list of dictionary (all with the same keys)
            
        except: 
            # When error occurs - most likely because comments are disabled on a video
            print('Comments disabled for the video ' + video_id)
        
    return pd.DataFrame(all_comments)  # return a df with the list of dictionary 