import psycopg
from .config import DB_CONFIG
 
db_config = DB_CONFIG

def fetch_all():
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cur:
            cur.execute(PSQL_SELECT_ALL)
            rows = cur.fetchall()

            for record in rows:
                print(record)

def count_entries():
        with psycopg.connect(**db_config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM quotes")
                res = cur.fetchone()[0]

                print('entries in quotes: ' + str(res))

PSQL_SELECT_ALL = '''
    SELECT * FROM quotes;
    '''
PSQL_RESET_SELECTED = '''
    UPDATE your_table
    SET selected = TRUE
    WHERE selected = FALSE;
'''

PSQL_CREATE_QUOTES_TABLE = '''
    CREATE TABLE IF NOT EXISTS public.quotes
(
    quote text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default",
    title text COLLATE pg_catalog."default",
    page integer,
    selected boolean DEFAULT false,
    id integer NOT NULL DEFAULT nextval('quotes_id_seq'::regclass),
    CONSTRAINT quotes_pkey PRIMARY KEY (id)
)
    '''

#TODO: implement update quote by id
PSQL_UPDATE_QUOTE = '''
    '''

#TODO: set all quotes.selected to FALSE
PSQL_SET_ALL_SELECTED_FALSE = '''
    '''



if __name__ == '__main__':
    count_entries()