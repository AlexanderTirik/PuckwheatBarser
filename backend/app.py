from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)


@app.route("/")
async def index(request):
    return json({"api": "v1"})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
        auto_reload=True
    )
