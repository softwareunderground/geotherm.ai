#-*- coding: utf-8 -*-
import sys

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles


version = f"{sys.version_info.major}.{sys.version_info.minor}"


app = FastAPI(
    title="geotherm.ai",
    description="Random geothermal applets",
    version="0.1",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def main():
    return "Hello"
