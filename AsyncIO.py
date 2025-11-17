import time
import requests

# def download_file(name):
#     print(f"Downloading {name}...")
#     with requests.get("https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg", stream=True) as resp:
#         resp.raise_for_status()
#         with open(f"{name}.jpg", "wb") as f:
#             for chunk in resp.iter_content(chunk_size=8192):
#                 if chunk:
#                     f.write(chunk)
    

#     time.sleep(3)
#     print(f"{name} downloaded!")

# def main():
#     download_file("file1")
#     download_file("file2")

# main()



import asyncio

def _download_sync(name):
    with requests.get("https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg", stream=True) as resp:
        resp.raise_for_status()
        with open(f"{name}.jpg", "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

async def download_file(name):
    print(f"Downloading {name}...")
    # run blocking download in a thread so the event loop isn't blocked
    await asyncio.to_thread(_download_sync, name)
    await asyncio.sleep(3)
    print(f"{name} downloaded!")

async def main():
    task1 = asyncio.create_task(download_file("file1"))
    task2 = asyncio.create_task(download_file("file2"))
    
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())
