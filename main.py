from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import requests
import logging

logger = logging.getLogger("search")
app = FastAPI()

import os
SERPER_API_KEY = os.environ.get("SERPER_API_KEY", "")

@app.get("/")
def read_root():
    with open("index.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())


@app.get("/output.css")
def get_css():
    return FileResponse("output.css")


@app.get("/search")
def search(q: str):
    try:
        resp = requests.post(
            "https://google.serper.dev/search",
            json={"q": q, "num": 10},
            headers={"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"},
            timeout=8,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        logger.error("Serper API failed: %s", e)
        return {"query": q, "results": [], "error": "search_unavailable"}

    results = [
        {"title": item.get("title"), "link": item.get("link")}
        for item in data.get("organic", [])
    ]
    return {"query": q, "results": results}