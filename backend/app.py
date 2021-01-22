from itertools import chain

from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

from backend.parsers import (
    parse_fozzy, parse_epicentrk
)

app = Sanic(__name__)
CORS(app)
sem = None


# @app.listener('before_server_start')
# def init(sanic, loop):
#     global sem
#     concurrency_per_worker = 4
#     sem = asyncio.Semaphore(concurrency_per_worker, loop=loop)


@app.route("/")
async def index(request):
    return json({"api": "v1"})


@app.route("get_data")
async def get_data(request):
    data_fozzy = await parse_fozzy()
    data_epicentrik = await parse_epicentrk()
    # next calls of parsers

    data = list(chain(data_fozzy, data_epicentrik))
    return json(data)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
        auto_reload=True
    )
