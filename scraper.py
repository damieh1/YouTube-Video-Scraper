import os
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import yt_dlp
import pandas as pd

###############################
### API key and Playlist ID ###
###############################
api_key = 'Add your YT API-key here'
playlist_id = 'Add your Playlist ID here'

def get_videos_from_playlist(youtube, playlist_id):
    videos = []
    next_page_token = None

    while True:
        try:
            playlist_request = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            playlist_response = playlist_request.execute()

            for item in playlist_response['items']:
                video_id = item['snippet']['resourceId']['videoId']
                title = item['snippet']['title']
                videos.append({'VideoID': video_id, 'Title': title})

            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break
        except HttpError as e:
            print(f"An error occurred: {e}")
            break

    return videos

def download_video_yt_dlp(video_id, title, save_path='videos'):
    url = f'https://www.youtube.com/watch?v={video_id}'
    print(f"Attempting to download: {url}")
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(save_path, f'{title}.%(ext)s'),
        'quiet': False,
        'verbose': True  # Increase verbosity for debugging
    }
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f'Downloaded: {title}')
        except Exception as e:
            print(f"An error occurred while downloading {title}: {e}")

def main(api_key, playlist_id):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    
    # Videos from playlist
    videos = get_videos_from_playlist(youtube, playlist_id)
    
    # Creating Pands df
    videos_df = pd.DataFrame(videos)
    print(videos_df)

    # Download videos
    for video in videos:
        download_video_yt_dlp(video['VideoID'], video['Title'])

if __name__ == '__main__':
    main(api_key, playlist_id)
