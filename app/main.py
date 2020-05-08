#-*- coding: utf-8 -*-
import sys

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import geomodels


version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI(
    title="geotherm.ai",
    description="Random geothermal applets",
    version="0.1",
)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def main(request: Request):

    q = ''

    context = {
        'request': request,
    }

    return templates.TemplateResponse("index.html", context)

@app.get("/about")
def about(request: Request):

    context = {
        'request': request,
    }

    return templates.TemplateResponse("about.html", context)

@app.get("/world-map")
def world(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("world_map.html", context)

@app.get("/us-map")
def us(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("us_map.html", context)

@app.get("/query")
def query(request: Request, q: str = ''):

    recs = geomodels.georecommend(q)

    result = []
    for rec in recs[1:]:
        print('in loop')
        result.append({'title': rec[2], 'link': rec[10]})

    context = {
        'request': request,
        'result': result,
    }

    return templates.TemplateResponse("index.html", context)

@app.get("/api")
def api(request: Request, q: str = ''):

    if not q:
        context = {
            'request': request,
        }

        return templates.TemplateResponse("api.html", context)

    result = {
        'parameters': {'word': q},
        'result': [
            {'url': 'URL 0',
             'title': 'TITLE 0',
             },
            {'url': 'URL 1',
             'title': 'TITLE 1',
             },
        ]
    }

    return result
