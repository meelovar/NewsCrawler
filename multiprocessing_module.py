import sqlite3
from functools import partial
from multiprocessing import Pool

from requests_module import get_links
from selenium_module import CookiesUpdater
from sqlite_module import get_profiles, DEFAULT_DB_NAME


def run():
    with sqlite3.connect(DEFAULT_DB_NAME) as connection:
        profile = get_profiles(connection)

    links = get_links()
    updaters = [CookiesUpdater(p) for p in profile]

    print(f"Found {len(links)} links")

    with Pool(5) as pool:
        pool.map(partial(_internal, links), updaters)


def _internal(links, updater):
    updater.open_random_link(links)
