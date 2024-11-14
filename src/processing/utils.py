import os
import asyncio

async def save_detail(output_path:str,data:str) -> None:
    with open(f"{output_path}/data.txt", "w") as f:
        f.write(data)

async def save_url_list(data:str) -> None:
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/../../url_list.txt", "w") as f:
        f.write(data)