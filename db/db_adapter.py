import psycopg
from config import DB_CONFIG



db_config = DB_CONFIG

with psycopg.connect(**db_config) as conn:

    with conn.cursor() as cur:

        cur.execute("SELECT * FROM quotes")
        rows = cur.fetchall()

        for record in rows:
            print(record)

        conn.commit()

print('finished')