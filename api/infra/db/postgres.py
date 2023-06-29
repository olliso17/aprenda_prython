import os
import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.environ['host'],
            port=os.environ['port'],
            database=os.environ['database'],
            user=os.environ['user'],
            password=os.environ['password'],
        )

    def execute_query(self, query, values=None):
        with self.connection.cursor() as cursor:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
        self.connection.commit()
        return result