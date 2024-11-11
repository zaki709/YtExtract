import sys
import os
import subprocess as sbp

script_dir = os.path.dirname(os.path.abspath(__file__))

def download_video(url:str, format:str="mp3"):
    if format == "mp3":
        proc = sbp.run(f"yt-dlp -x --audio-format {format} {url}", shell=True,cwd=f"{script_dir}/../../output/")    
    else:
        proc = sbp.run(f"yt-dlp --format {format} {url}", shell=True,cwd=f"{script_dir}/../../output/")
    inline = proc.stdout
    print(inline)

if __name__ == '__main__':
    download_video(sys.argv[1])