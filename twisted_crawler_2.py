from txmongo import MongoConnection
from treq import get
from twisted.internet import defer, reactor


def parse(text):
    return dict(text=text)


@defer.inlineCallbacks
def download_urls(url_list):
    mongo_client = yield MongoConnection()

    @defer.inlineCallbacks
    def download_url(url):
        """Download and store single url"""
        response = yield get(url)

        d = parse((yield response.text()))

        yield mongo_client.test.pages.insert(d)

    yield defer.gatherResults(download_url(url) for url in url_list)


urls = [
    'https://en.wikipedia.org/wiki/Saguaro_National_Park',
    'https://en.wikipedia.org/wiki/Saguaro',
    'https://en.wikipedia.org/wiki/The_Power_of_Sympathy',
    'http://cienciaconelpueblo.org'
]


download_urls(urls).addCallback(lambda ign: reactor.stop())
reactor.run()
