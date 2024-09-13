import psycopg2

from database_config.config import DB_CONFIG


class DBSettings:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()

        if self.conn is not None:
            self.conn.close()

        if self.cursor is not None:
            self.cursor.close()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()


def execute_query(query, params=None, fetch=None):
    try:
        with DBSettings() as db:
            if fetch == "all":
                return db.fetchall(query, params)
            elif fetch == "one":
                return db.fetchone(query, params)
            else:
                db.execute(query, params)
    except Exception as e:
        print(f"Exception occurred while executing: {e}")