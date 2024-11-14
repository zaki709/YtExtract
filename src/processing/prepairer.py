import os
import asyncio

script_dir = os.path.dirname(os.path.abspath(__file__))

async def prepair(dir_name:str) -> dict | None:
    if not os.path.exists(f"{script_dir}/../../output/{dir_name}"):
        base = f"{script_dir}/../../output/{dir_name}"
        os.mkdir(base)
        os.mkdir(base + "/image")
        os.mkdir(base + "/sound")
        os.mkdir(base + "/data")
        return {"base": base,"image": base + "/image", "sound": base + "/sound", "data": base + "/data"}
    else:
        print(f"Path {dir_name} already exists")