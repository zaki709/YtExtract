import asyncio
import os
import sys

from processing.downloader import download_video, download_thumbnail
from processing.parser import youtube_video_parser
from processing.prepairer import prepair
from processing.converter import mp4_to_wav
from processing.utils import save_detail

script_dir = os.path.dirname(os.path.abspath(__file__))

async def main(url:str) -> None:
    title, thumbnail = await youtube_video_parser(url)
    path_dict = await prepair(title)
    print(path_dict)
    await download_video(url, path_dict["base"],title)
    await download_thumbnail(thumbnail, path_dict["image"])
    await mp4_to_wav(f"{path_dict['base']}/{title}.mp4", f"{path_dict['sound']}/{title}.wav")
    await save_detail(path_dict["data"], url)
    os.remove(f"{path_dict['base']}/{title}.mp4")

if __name__ == '__main__':
    asyncio.run(main(sys.argv[1]))