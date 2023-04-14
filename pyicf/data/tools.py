"""Tools for 'pyicf.data module"""
from datetime import datetime

def int_to_datetime(int_date: str|int, strformat: str):
    """Converts an timestamp integer into a datetime representation"""
    date = datetime.fromtimestamp(int(int_date) / 1e3)
    return date.strftime(strformat)
