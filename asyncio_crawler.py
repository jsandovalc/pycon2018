import asyncio
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient


def parse(text):
    return dict(text=text)

async def download_urls(url_list):
    client = ClientSession()

    mongo_client = AsyncIOMotorClient()

    for url in url_list:
        response = await client.get(url)
        d = parse(await response.text())

        await mongo_client.test.pages.insert_one(d)

    await client.close()

urls = [
    'https://en.wikipedia.org/wiki/Saguaro_National_Park',
    'https://en.wikipedia.org/wiki/Saguaro',
    'https://en.wikipedia.org/wiki/The_Power_of_Sympathy',
    'http://cienciaconelpueblo.org'
]


loop = asyncio.get_event_loop()
loop.run_until_complete(download_urls(urls))
