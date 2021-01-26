from itertools import chain
import os

from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

from src.parsers import parse_fozzy, parse_epicentrk, parse_auchan
from src.services import get_response, sort_by_price
from src.consts import FOZZY_URL, EPICENTRK_URL, AUCHAN_URL

app = Sanic(__name__)
CORS(app)
last_data = []


@app.route("/")
async def index(request):
    return json({"api": "v1"})


@app.route("get_data")
async def get_data(request):
    global last_data

    sort_order = request.args.get("sort")
    if sort_order:
        data = sort_by_price(last_data, order=sort_order) or last_data
    else:
        response_fozzy = await get_response(FOZZY_URL)
        response_epicentrk = await get_response(EPICENTRK_URL)
        response_auchan = await get_response(AUCHAN_URL)

        data_fozzy = parse_fozzy(response_fozzy)
        data_epicentrk = parse_epicentrk(response_epicentrk)
        data_auchan = parse_auchan(response_auchan)

        data = list(chain(data_fozzy, data_epicentrk, data_auchan)) or last_data
        last_data = data

    return json(
        {
            "buckwheatData": data,
            "sort": sort_order,
        }
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", port=8000, debug=os.getenv("DEBUG", False), auto_reload=True
    )
