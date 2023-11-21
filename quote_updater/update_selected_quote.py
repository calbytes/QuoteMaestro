import psycopg
from .config import DB_CONFIG
import random

db_config = DB_CONFIG

def select_quote_id():
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
                #retrieve ids of entries where selected = False
                cur.execute('''
                    SELECT id FROM quotes 
                    WHERE selected = 'false';
                ''')
                rows = cur.fetchall()

                if not rows:
                    raise ValueError("No rows found with selected = FALSE")
                    
                #generage random number and get quote id
                random_num = random.randrange(len(rows))
                id = rows[random_num][0]
                return id
        
def update_selected_quotes(id):
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
            #update entry selected = True
            cur.execute('''
                UPDATE quotes 
                SET selected = TRUE 
                WHERE id = %s;
            ''', (id,))

            #add id to selected_quotes
            cur.execute('''
                INSERT INTO selected_quotes 
                (quote_id) VALUES (%s);
            ''', (id,))
