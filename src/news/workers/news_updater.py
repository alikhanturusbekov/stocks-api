import datetime
import logging
import time
from multiprocessing.pool import ThreadPool

from apscheduler.schedulers.background import BackgroundScheduler

from ..services import save_company_news
from ..constants import SUPPORTED_STOCKS


def save_company_news_job():
    logging.info("STARTING NEWS UPDATER...")
    start = time.time()

    pool = ThreadPool()
    pool.map(save_company_news, SUPPORTED_STOCKS)

    end = time.time() - start
    logging.info(f"NEWS UPDATER has finished in {end}")


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        save_company_news_job,
        'interval',
        id='retrieve_company_news',
        next_run_time=datetime.datetime.now(),
        hours=1,
        replace_existing=True
    )
    scheduler.start()
