import asyncio

async def save_detail(output_path:str,data:str) -> None:
    with open(f"{output_path}/data.txt", "w") as f:
        f.write(data)