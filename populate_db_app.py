import quote_factory.tokenizer as qt
import db_manager.insert_quotes as db
import db_manager.db_queries as db_queries

def insert_quote_entries():
    quotes = qt.get_quote_entries()
    db.populate_db(quotes)
    print('insert_quote_entries() finished')

def fetch_all():
    db_queries.fetch_all()

def count_entries():
    db_queries.count_entries()

if __name__ == '__main__':
    #insert_quote_entries()
    print('qm_app() finished')