import psycopg

class DatabaseFactory:
    def __init__(self, db_params):
        self.db_params = db_params

    def create_connection(self):
        return psycopg.connect(**self.db_params)

    def create_cursor(self):
        conn = self.create_connection()
        return conn.cursor()

    def close_connection(self, conn):
        conn.close()

    def commit_transaction(self, conn):
        conn.commit()

    def rollback_transaction(self, conn):
        conn.rollback()
