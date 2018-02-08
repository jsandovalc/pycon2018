import treq
from klein import Klein
app = Klein()

@app.route('/')
async def google(request):
    response = await treq.get(b'https://www.google.com')
    content = await treq.content(response)
    return content

app.run("localhost", 8080)
