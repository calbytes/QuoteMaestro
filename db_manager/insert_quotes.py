import psycopg
from .config import DB_CONFIG
 
db_config = DB_CONFIG

def populate_db(quotes):
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
            for entry in quotes:
                cur.execute('''
                    INSERT INTO quotes (quote, title, author, page) 
                            VALUES (%s, %s, %s, %s, %s);
                ''', (entry.quote, entry.title, entry.author, entry.page))

            conn.commit()

if __name__ == '__main__':
    populate_db()
    print('populate_db finished')