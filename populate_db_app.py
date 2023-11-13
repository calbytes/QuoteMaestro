import quote_factory.tokenizer as qt
import db_manager.insert_quotes as db

def insert_quote_entries():
    quotes = qt.get_quote_entries()
    db.populate_db(quotes)
    print('insert_quote_entries() finished')
    
if __name__ == '__main__':
    #insert_quote_entries()
    print('qm_app() finished')