from aiohttp import web

async def handle(request):
    #    print('request.json():', await request.json())
    print('request.text():', await request.text())
    print('request.headers:', request.headers)
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    print('return %s' % text)
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)
app.router.add_post('/', handle)
app.router.add_post('/{name}', handle)
# not detecting Ctrl+C for windows
web.run_app(app, host='127.0.0.1', port=8080)

# curl -X POST "http://127.0.0.1:8080/" -H "Content-Type:
# application/json" -H "name:HEADER NAME" -d "{\"name\":\"BODY NAME\"}"
