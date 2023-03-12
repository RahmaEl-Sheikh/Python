import requests
import time


def fetch_data_sync(url):
    response = requests.get(url)
    return response.json()


urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
    "https://jsonplaceholder.typicode.com/posts/6",
    "https://jsonplaceholder.typicode.com/posts/7",
    "https://jsonplaceholder.typicode.com/posts/8",
    "https://jsonplaceholder.typicode.com/posts/9",
    "https://jsonplaceholder.typicode.com/posts/10",
    "https://jsonplaceholder.typicode.com/posts/11",
    "https://jsonplaceholder.typicode.com/posts/12",
    "https://jsonplaceholder.typicode.com/posts/13",
    "https://jsonplaceholder.typicode.com/posts/14",
    "https://jsonplaceholder.typicode.com/posts/15",
    "https://jsonplaceholder.typicode.com/posts/16",
    "https://jsonplaceholder.typicode.com/posts/17",
    "https://jsonplaceholder.typicode.com/posts/18",
    "https://jsonplaceholder.typicode.com/posts/19",
    "https://jsonplaceholder.typicode.com/posts/20",
    "https://jsonplaceholder.typicode.com/posts/21",
    "https://jsonplaceholder.typicode.com/posts/22",
    "https://jsonplaceholder.typicode.com/posts/23",
    "https://jsonplaceholder.typicode.com/posts/24",
    "https://jsonplaceholder.typicode.com/posts/25",
    "https://jsonplaceholder.typicode.com/posts/26",
    "https://jsonplaceholder.typicode.com/posts/27",
    "https://jsonplaceholder.typicode.com/posts/28",
    "https://jsonplaceholder.typicode.com/posts/29",
    "https://jsonplaceholder.typicode.com/posts/30",
    "https://jsonplaceholder.typicode.com/posts/31",
    "https://jsonplaceholder.typicode.com/posts/32",
    "https://jsonplaceholder.typicode.com/posts/33",
    "https://jsonplaceholder.typicode.com/posts/34",
    "https://jsonplaceholder.typicode.com/posts/35",
    "https://jsonplaceholder.typicode.com/posts/36",
    "https://jsonplaceholder.typicode.com/posts/37",
    "https://jsonplaceholder.typicode.com/posts/38",
    "https://jsonplaceholder.typicode.com/posts/39",
    "https://jsonplaceholder.typicode.com/posts/40"
]

start_time = time.time()

for url in urls:
    data = fetch_data_sync(url)
    print(data['title'])

end_time = time.time()

print(f"Sync API calls took {end_time - start_time} seconds")

########################33

import asyncio
import aiohttp
import time

async def fetch_data_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_data = await response.json()
            return url, json_data

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

async def main_async():
    tasks = []
    for url in urls:
        tasks.append(asyncio.ensure_future(fetch_data_async(url)))
    responses = await asyncio.gather(*tasks)
    for url, json_data in responses:
        print(f"Response from {url}: {json_data}")

start_time = time.time()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main_async())

end_time = time.time()

print(f"Async API calls took {end_time - start_time} seconds")
