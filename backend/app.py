from itertools import chain

from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

from backend.parsers import (
    parse_fozzy, parse_epicentrk, parse_auchan
)

from backend.services import (
    get_response
)

from backend.urls import (
    FOZZY_URL, EPICENTRK_URL, AUCHAN_URL
)

app = Sanic(__name__)
CORS(app)
sem = None


@app.route("/")
async def index(request):
    return json({"api": "v1"})


@app.route("get_data")
async def get_data(request):
    response_fozzy = await get_response(FOZZY_URL)
    response_epicentrk = await get_response(EPICENTRK_URL)
    response_auchan = await get_response(AUCHAN_URL)

    data_fozzy = parse_fozzy(response_fozzy)
    data_epicentrk = parse_epicentrk(response_epicentrk)
    data_auchan = parse_auchan(response_auchan)
    
    data = list(chain(data_fozzy, data_epicentrk, data_auchan))
    return json(data)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
        auto_reload=True
    )
