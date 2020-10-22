""" Date and Time """
from datetime import datetime

from common.constant import DATEFORMAT, TIMEFORMAT


def date_time() -> datetime:
    return datetime.now()


def get_date() -> datetime:
    date = date_time()
    return date.strftime(DATEFORMAT)


def get_time() -> datetime:
    time = date_time()
    return time.strftime(TIMEFORMAT)
