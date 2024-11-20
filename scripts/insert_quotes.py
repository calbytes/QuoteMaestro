import quote_factory.tokenizer as tokenizer
import db_manager.db_client as db

def insert_all_quote_entries():
    print("insert_quote_entries() starting")
    quotes = tokenizer.get_all_quote_entries_in_dir()
   
    for quote in quotes:
        data = (quote.quote, quote.author, quote.title, quote.page, 'false')
        db.insert_quote(data)

    print('insert_quote_entries() finished')

def insert_quote_entries_for_book():
    file_name = input("Enter file name: ").strip()
    quotes = tokenizer.get_quote_entries_for_file(file_name)
    for quote in quotes:
        data = (quote.quote, quote.author, quote.title, quote.page, 'false')
        db.insert_quote(data)

    print("finished insert_quote_entries_for_book()")

    
if __name__ == '__main__':
    #insert_all_quote_entries()
    insert_quote_entries_for_book()
    print('\n--->>> insert_quotes() finished')