import asyncio
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient


def parse(text):
    return dict(text=text)

async def download_url(url, client):
    response = await client.get(url)
    d = parse(await response.text())

    await mongo_client.test.pages.insert_one(d)


async def download_urls(url_list):
    async with ClientSession as client:
        mongo_client = AsyncIOMotorClient()

        await asyncio.gather(download_url(url, client) for url in url_list)

urls = [
    'https://en.wikipedia.org/wiki/Saguaro_National_Park',
    'https://en.wikipedia.org/wiki/Saguaro',
    'https://en.wikipedia.org/wiki/The_Power_of_Sympathy',
    'http://cienciaconelpueblo.org',
]

loop = asyncio.get_event_loop()
loop.run_until_complete(download_urls(urls))
