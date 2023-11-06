import getpass
import psycopg

def select_one(sql_raw, params):
    """ Runs SELECT query that will return zero or 1 rows.  `params` is required."""
    return _execute_query(sql_raw, params, 'sel_single')


def select_multi(sql_raw, params=None):
    """ Runs SELECT query that will return multiple.  `params` is optional."""
    return _execute_query(sql_raw, params, 'sel_multi')


def insert(sql_raw, params):
    """ Runs Insert query, returns result.
    Returned result is typically the newly created PRIMARY KEY value from the database.
    """
    return _execute_query(sql_raw, params, 'insert')


def update(sql_raw, params):
    """ Runs UPDATE query, returns result depending on update query executed."""
    return _execute_query(sql_raw, params, 'update')


def get_db_string():
    database_string = 'postgresql://{user}:{pw}@{host}:{port}/{dbname}'
    db_name = input('Database name: ')
    db_user = input('Enter PgSQL username: ')
    db_pw = getpass.getpass('Enter password: ')
    db_host = input('Database host [127.0.0.1]: ') or '127.0.0.1'
    db_port = input('Database port [5432]: ') or '5432'
    
    return database_string.format(user=db_user, pw=db_pw, host=db_host,
                                  port=db_port, dbname=db_name)


def get_db_conn():
    db_string = get_db_string()

    try:
        conn = psycopg.connect(db_string)
    except psycopg.OperationalError as err:
        err_msg = 'DB Connection Error - Error: {}'.format(err)
        print(err_msg)
        return False
    return conn


def _execute_query(sql_raw, params, qry_type):
    """ Handles executing all types of queries based on the `qry_type` passed in.
    Returns False if there are errors during connection or execution.
        if results == False:
            print('Database error')
        else:
            print(results)
    You cannot use `if not results:` b/c 0 results is a false negative.
    """
    try:
        conn = get_db_conn()
    except psycopg.ProgrammingError as err:
        print('Connection not configured properly.  Err: %s', err)
        return False

    if not conn:
        return False

    cur = conn.cursor(cursor_factory=psycopg.extras.DictCursor)

    try:
        cur.execute(sql_raw, params)
        if qry_type == 'sel_single':
            results = cur.fetchone()
        elif qry_type == 'sel_multi':
            results = cur.fetchall()
        elif qry_type == 'insert':
            results = cur.fetchone()
            conn.commit()
        elif qry_type == 'update':
            results = cur.fetchone()
            conn.commit()
        else:
            raise Exception('Invalid query type defined.')

    except psycopg.ProgrammingError as err:
        print('Database error via psycopg2.  %s', err)
        results = False
    except psycopg.IntegrityError as err:
        print('PostgreSQL integrity error via psycopg2.  %s', err)
        results = False
    finally:
        conn.close()

    return results