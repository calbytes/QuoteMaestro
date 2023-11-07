import psycopg
from config import DB_CONFIG
import 

db_config = DB_CONFIG

quotes = tokenizer.get_quote_entries()
print(quotes)
exit()

with psycopg.connect(**db_config) as conn:
    with conn.cursor() as cur:

        cur.execute("SELECT * FROM quotes")
        rows = cur.fetchall()

        for record in rows:
            print(record)

        conn.commit()

print('finished')