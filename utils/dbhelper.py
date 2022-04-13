import os

import psycopg2

class DbHelper():
    def __init__(self):
        self.mydb = None
        self.cursor = None

    def open(self):
        try:
            self.mydb = psycopg2.connect(host = os.getenv('dbhost'), user = os.getenv('dbuser'), password = os.getenv('dbpw'), database = os.getenv('db_db'), port = os.getenv('dbport'))
        except psycopg2.Error as e:
            print(f'Error connecting to the platform (mydb): {e}')

        # getting the cursor
        try:
            self.cursor = self.mydb.cursor()
        except psycopg2.Error as c:
            print(f'Error connecting to the platform (cursor): {c}')
        return self.mydb

    def close(self):
        try:
            self.cursor.close()
            self.mydb.close()
        except psycopg2.Error as ce:
            print(f'Error while closing the database: {ce}')

    def get_cursor(self):
        return self.cursor