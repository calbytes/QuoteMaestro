import psycopg
from .config import DB_CONFIG
from db_manager.psql_queries import PSQL_QUERIES as psql
from enum import Enum, auto

class Fetch(Enum):
    ONE = auto()
    ALL = auto()
    EXC = auto()

class DB_CLIENT:
    def __init__(self):
        self.config = DB_CONFIG

    def execute(self, psql_raw, fetch: Fetch, params=None):
        try:
            with psycopg.connect(**self.config) as conn:
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

    def insert_quote(self, data):
        self.execute(psql.INSERT_QUOTE, Fetch.EXC, data)

    def get_all_quotes(self):
        rows = self.execute(psql.SELECT_ALL_QUOTES, Fetch.ALL)
        return rows

    def get_reviewed_keywords(self, data):
        row = self.execute(psql.GET_REVIEWED_KEYWORDS, Fetch.ONE, data)
        return row


