import time

from multiprocessing_module import run
from sqlite_module import DEFAULT_DB_NAME, init_database


def main():
    init_database(DEFAULT_DB_NAME)

    try:
        while True:
            run()
            time.sleep(600)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
