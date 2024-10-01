import psycopg
from .config import DB_CONFIG
from db_manager.psql_queries import PSQL_QUERIES as psql
from enum import Enum, auto

class Fetch(Enum):
    ONE = auto()
    ALL = auto()
    EXC = auto()

config = DB_CONFIG

def execute(psql_raw, fetch: Fetch, params=None):
    try:
        with psycopg.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(psql_raw, params)

                if fetch == Fetch.ONE:
                    row = cur.fetchone()
                    return row
                elif fetch == Fetch.ALL:
                    rows = cur.fetchall()
                    return rows
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def update_quote(data):
    execute(psql.UPDATE_QUOTE, Fetch.EXC, data)

def get_all_quotes():
    rows = execute(psql.SELECT_ALL_QUOTES, Fetch.ALL)
    return rows

def insert_quote(data):
    execute(psql.INSERT_QUOTE, Fetch.EXC, data)


