import json
import random
import sqlite3
import time

from selenium import webdriver
from selenium.common import InvalidCookieDomainException

from sqlite_module import DEFAULT_DB_NAME, update_cookies


class CookiesUpdater:
    def __init__(self, profile):
        self.profile_id = profile["id"]
        self.cookies = profile["cookie"]

    def open_random_link(self, links):
        link = random.choice(links)

        with webdriver.Firefox() as driver:
            print(f"Start {link}")
            driver.get(link)

            try:
                for cookie in self.cookies:
                    driver.add_cookie(cookie)
            except InvalidCookieDomainException:
                pass
            else:
                driver.refresh()

            self.__scroll(random.randint(1, 10), driver)

            cookies = driver.get_cookies()

        print(f"Stop {link}")

        with sqlite3.connect(DEFAULT_DB_NAME) as connection:
            update_cookies(connection, self.profile_id, json.dumps(cookies))

    @staticmethod
    def __scroll(delay, driver):
        time.sleep(delay)
        driver.execute_script("window.scrollByLines(1000);")
