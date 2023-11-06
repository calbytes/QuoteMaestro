import psycopg2

connection = psycopg2.connect(
            host = "192.168.1.45",
            database="calirig_db",
            user = "postgres",
            password = "Snaaake___Plaaant?1010!")

cursor = connection.cursor()

cursor.execute("insert into quotes (quote, title, author, page) values (%s, %s, %s)", ("test string", "test title", "test author", 1) )

cursor.execute("select quote, title, author, page from quotes")
rows = cursor.fetchall()

for row in rows:
    print(row)

#Commit any pending transaction to the database.
connection.commit()

cursor.close()
connection.close()