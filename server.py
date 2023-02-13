from sanic import Sanic, response

app = Sanic("MySanicApp")

@app.get('/')
async def hello(request):
    return response.json({"state": "healthy", "gpu": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)