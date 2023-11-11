from db_factory import DatabaseFactory
from .config import DB_CONFIG
 
db_config = DB_CONFIG

factory = DatabaseFactory(db_config)

cursor = factory.create_cursor()

cursor.execute('SELECT * FROM quotes')
rows = cursor.fetchall()
for record in rows:
    print(record)
    
cursor.close()
