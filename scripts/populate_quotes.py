import quote_factory.tokenizer as qt
import db_manager.db_client as db_client

def insert_quote_entries():
    quotes = qt.get_quote_entries()
    
    for quote in quotes:
        data = (quote,)
        db_client.insert_quote(data)
    print('insert_quote_entries() finished')
    
if __name__ == '__main__':
    #insert_quote_entries()
    print('--->>> populate_db() finished')