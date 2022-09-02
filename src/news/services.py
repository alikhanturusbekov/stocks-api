import datetime
import logging
from zoneinfo import ZoneInfo

from .finnhub.client import finnhub_client
from .models import CompanyNews


def save_company_news(stock: str) -> None:
    for new in _get_company_news(stock):
        if _exists_company_news(new['id']):
            continue

        time_ = datetime.datetime.fromtimestamp(new['datetime'])

        try:
            CompanyNews.objects.create(
                id=new['id'],
                stock=new['related'],
                headline=new['headline'],
                image=new['image'],
                summary=new['summary'],
                source=new['source'],
                url=new['url'],
                published_at=time_.astimezone(ZoneInfo("UTC")),
            )
        except Exception:
            logging.error(f'News with id of {new["id"]} cannot be saved.')


def _get_company_news(stock: str) -> list:
    _from = datetime.date.today() - datetime.timedelta(days=30)
    to = datetime.date.today()

    news = finnhub_client.company_news(stock, _from=_from, to=to)

    return news


def _exists_company_news(id_: int) -> bool:
    try:
        CompanyNews.objects.get(id=id_)
        return True
    except Exception:
        return False


# ---- ! async attempt failed due to synchronous django ORM ----
#
# async def _get_one_news(session, url):
#     async with session.get(url) as res:
#         news_data = await res.json()
#         return news_data
#
#
# async def _get_company_news():
#     result = []
#     _from = datetime.date.today() - datetime.timedelta(days=30)
#     to = datetime.date.today()
#
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#
#         for stock in SUPPORTED_STOCKS:
#             url = f"https://finnhub.io/api/v1/company-news?token={api_key}&symbol={stock}&from={_from}&to={to}"
#             tasks.append(asyncio.ensure_future(_get_one_news(session, url)))
#
#         res = await asyncio.gather(*tasks)
#
#     for stock_news in res:
#         result.extend(stock_news)
#
#     return result
