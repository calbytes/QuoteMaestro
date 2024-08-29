from db_manager.db_client import DB_CLIENT
from textblob import TextBlob

db = DB_CLIENT()

def proof_read_quotes():
    quotes = db.get_all_quotes()
    for row in quotes:
        quote = row[0].strip()
        quote_id = row[5]
        print(quote_id)

        blob = TextBlob(quote)
        corrected_quote = str(blob.correct())

        data = (corrected_quote, quote_id)
        db.update_quote(data)

if __name__== '__main__':
    print("Starting proof_read_quotes()")
    #proof_read_quotes()
    print("--->>> proof_read_quotes() FINISHED")