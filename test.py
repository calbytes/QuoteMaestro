import quote_updater.quote_selector as dbt
import db_manager.PSQL_QUERIES as db

def tester():
    print('calling db.fetch_all()')
    db.fetch_all()

def tester():
    print(str(dbt.select_quote_entry()))

if __name__ == '__main__':
    tester()