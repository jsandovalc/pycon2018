from sanic import Sanic
from sanic.response import html
from aiohttp import ClientSession

app = Sanic()

@app.route("/")
async def test(request):
    client = ClientSession()
    response = await client.get('https://www.google.com')
    content = await response.text()
    return html(content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
