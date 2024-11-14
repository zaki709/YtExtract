import os
import subprocess as sbp
import asyncio
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))

async def download_video(url:str, output_path:str,name:str,format:str="mp4") -> bool:
    if not os.path.exists(output_path):
        print(f"Path {output_path} does not exist")
        return False
    else:
        proc = sbp.run(f"yt-dlp --format {format} -o {name}.mp4 {url}", shell=True,cwd=output_path)
        _ = proc.stdout
        return True

async def download_thumbnail(url:str,output_path:str) -> bool:
    if not os.path.exists(output_path):
        print(f"Path {output_path} does not exist")
        return False
    else:
        res = requests.get(url)
        with open(f"{output_path}/thumbnail.jpg", "wb") as f:
            f.write(res.content)
