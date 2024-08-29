from db_manager.db_client import DB_CLIENT

db = DB_CLIENT()

def proof_read_quotes():
    quotes = db.get_all_quotes()
    for quote in quotes:
        print(quote[0], quote[5])
        if True:
            break

if __name__== '__main__':
    print("Starting proof_read_quotes()")
    proof_read_quotes()
    print("--->>> proof_read_quotes() FINISHED")