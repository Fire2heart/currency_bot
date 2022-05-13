import sqlite3
from config import currencies_list, DATABASE, TABLE
from api import pull_in_base
from datetime import datetime

currencies = currencies_list.copy()
currencies.remove('USD')


def time_config() -> list:
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    return time


def init_table():
    columns = f'CREATE TABLE IF NOT EXISTS {TABLE} (ID INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT'
    for item in currencies:
        columns += f', {item} REAL'
    columns += ');'

    with sqlite3.connect(DATABASE) as db:
        db.execute(columns)


def insert(data: dict):
    with sqlite3.connect(DATABASE) as db:
        query = f'INSERT INTO {TABLE} (id, date'
        for item in currencies:
            query += f', {item}'
        query += ') VALUES (NULL, ?'
        for item in range(len(currencies)):
            query += ', ?'
        query += ');'

        temp = list(data.values())
        temp.insert(0, time_config())

        db.execute(query, (tuple(temp)))


init_table()
info = pull_in_base(currencies)
insert(info)
