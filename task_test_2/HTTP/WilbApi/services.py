import os
import asyncio
import aiohttp
import logging
import base64
import pandas
from .models import *
from pydantic import BaseModel, ValidationError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HTTP.settings")
import django

django.setup()

log = logging.getLogger(__name__)


class Article(BaseModel):
    nm_id: int
    imt_name: str
    selling: dict


async def get_search(artic):

    url = f"https://wbx-content-v2.wbstatic.net/ru/{artic}.json"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:

                try:
                    scrap_resolt = await response.json()
                    await search_articule(scrap_resolt)
                except ValidationError as err:
                    log.error(f"Error - {err}.")


async def search_articule(scrap_resolt):
    scrap_art = Article.parse_obj(scrap_resolt)
    sellin = scrap_art.selling
    article = scrap_art.nm_id
    brand = sellin["brand_name"]
    title = sellin["brand_name"] + "/" + scrap_art.imt_name
    await ProductArticle.objects.filter(article=article).aupdate(brand=brand, title=title)


async def get_search_file(articles):

    url = f"https://wbx-content-v2.wbstatic.net/ru/{articles}.json"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:

                try:
                    scrap_resolts = await response.json()
                    await search_articule(scrap_resolts)
                except ValidationError as err:
                    log.error(f"Error - {err}.")


async def search_art_excel(scrap_resolts):
    scrap_art = Person.parse_obj(scrap_resolts)
    sellin = scrap_art.selling
    article = scrap_art.nm_id
    brand = sellin["brand_name"]
    title = sellin["brand_name"] + "/" + scrap_art.imt_name
    await ExcelArticle.objects.filter(article=article).aupdate(brand=brand, title=title)


async def art_excel(excel_base64):
    excel_file = base64.b64decode(excel_base64)
    df = pandas.read_excel(excel_file)
    art_list = []
    for row in df.iterrows():
        art = row[1].to_list()
        art_list.append(art[0])
    await sending_article(art_list)


async def sending_article(art_list):
    await asyncio.gather(
        *(get_search_file(articles) for articles in art_list),
        return_exceptions=True
    )
