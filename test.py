import quote_updater.update_selected_quote as qu
import db_manager.PSQL_QUERIES as db

def tester():
    print('calling db.fetch_all()')
    db.fetch_all()

def tester():
    print(qu.select_quote_id)

if __name__ == '__main__':
    tester()