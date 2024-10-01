import quote_factory.tokenizer as qt
import db_manager.db_client as db

def insert_quote_entries():
    print("insert_quote_entries() starting")
    quotes = qt.get_quote_entries()
   
    id=0
    for quote in quotes:
        id += 1
        print("id: " + str(id))

        data = (id, quote.quote, quote.author, quote.title, quote.page, 'false')
        print(data)
        db.insert_quote(data)
    print('insert_quote_entries() finished')
    
if __name__ == '__main__':
    insert_quote_entries()
    print('--->>> populate_db() finished')