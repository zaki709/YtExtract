import os
import asyncio

script_dir = os.path.dirname(os.path.abspath(__file__))

async def mp4_to_wav(input_path:str,output_path:str) -> None:
    os.system(f"ffmpeg -i {input_path} -vn -acodec pcm_s16le -ar 44100 -ac 2 {output_path}")