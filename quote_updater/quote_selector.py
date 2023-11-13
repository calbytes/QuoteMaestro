import psycopg
from .config import DB_CONFIG
import random

db_config = DB_CONFIG

def select_quote_entry():
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
                #retrieve ids of entries with selected = False
                cur.execute('''
                    SELECT id FROM quotes 
                    WHERE selected = 'false';
                ''')
                rows = cur.fetchall()

                if not rows:
                    raise ValueError("No rows found with selected = FALSE")
                    
                #generage random number and get quote entry
                random_num = random.randrange(len(rows))
                id = rows[random_num]
                cur.execute('''
                    SELECT * FROM quotes 
                    WHERE id = %s;
                ''', (id))
                row = cur.fetchone()

                # Extract values from the row
                row_quote, row_author, row_title = row[0], row[1], row[2]

                #set entry selected to True
                cur.execute('''
                    UPDATE quotes 
                    SET selected = TRUE 
                    WHERE id = %s;
                ''', (id))

                print('id: ' + str(id))
                return row_quote, row_author, row_title

if __name__ == '__main__':
    select_quote_entry()
    print('DB_TEST() finished')