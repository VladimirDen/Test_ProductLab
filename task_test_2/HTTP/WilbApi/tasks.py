import asyncio

from HTTP.celery import app
from .services import get_search, art_excel


@app.task
def get_article(artic):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_search(artic))


@app.task
def get_file(excel_base64):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(art_excel(excel_base64))
