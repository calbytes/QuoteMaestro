import psycopg
from .config import DB_CONFIG
 
db_config = DB_CONFIG

def fetch_all():
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM quotes")
            rows = cur.fetchall()

            for record in rows:
                print(record)

def count_entries():
        with psycopg.connect(**db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM quotes")
                res = cur.fetchone()[0]

                print('entries in quotes: ' + str(res))

if __name__ == '__main__':
    count_entries()