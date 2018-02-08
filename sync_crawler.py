from pymongo import MongoClient
from requests import get


mongo_client = MongoClient()

def parse(text):
    return dict(text=text)


def download_urls(url_list):
    for url in url_list:
        response = get(url)
        d = parse(response.text)
        mongo_client.test.pages.insert_one(d)


urls = [
    'https://en.wikipedia.org/wiki/Saguaro_National_Park',
    'https://en.wikipedia.org/wiki/Saguaro',
    'https://en.wikipedia.org/wiki/The_Power_of_Sympathy',
    'http://cienciaconelpueblo.org'
]


download_urls(urls)
