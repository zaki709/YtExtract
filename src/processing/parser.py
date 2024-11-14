import os
import asyncio
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
APIKey = os.environ.get("YoutubDataAPIKey")

script_dir = os.path.dirname(os.path.abspath(__file__))

async def youtube_video_parser(url:str) -> tuple[str,str]:
    youtube = build('youtube', 'v3', developerKey=APIKey)
    id = url.split("/")[-1]
    if id.find("watch") != -1:
        id = id.split("=")[-1]
    response = youtube.videos().list(part='snippet', id=id).execute()
    title = response['items'][0]['snippet']['localized']['title']
    title = title.replace(" ", "_")
    thumbnail = response['items'][0]['snippet']['thumbnails']['default']['url']
    return (title, thumbnail)
