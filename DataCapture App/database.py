import mysql.connector as con

class Database:
    def __init__(self):
        self.conn = con.connect(
            host="localhost",
            user="root",
            password="Mysql2025@123",
            database="client_management"
        )
        self.cursor = self.conn.cursor(dictionary=True) 
    
    def execute(self, query, params=None, fetch=False):
        self.cursor.execute(query, params or ())
        if fetch:
            return self.cursor.fetchall()
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
