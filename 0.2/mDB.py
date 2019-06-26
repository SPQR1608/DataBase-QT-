from mysql.connector import MySQLConnection, Error
from config import read_db_config
from multipledispatch import dispatch

class mDataBase:
    def connect(self):
        """ Connect to MySQL database """

        db_config = read_db_config()

        try:
            print('Connecting to MySQL database...')
            conn = MySQLConnection(**db_config)

            if conn.is_connected():
                print('connection established.')
                return conn
            else:
                print('connection failed.')

        except Error as e:
            print(e)

    #@dispatch(str)
    def select(self, query):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            print('Total Row(s):', cursor.rowcount)
            #for row in rows:
             #   print(row)
            return rows
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            print('select: connection closed')

    #@dispatch(str, str)
    def select1(self, query, data):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            rows = cursor.fetchall()

            print('Total Row(s):', cursor.rowcount)
            for row in rows:
                print(row)
            return rows
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            print('select: connection closed')

    def insert(self, query, data):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            print('insert: connection closed')

    def update(self, query, data):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            print('update: connection closed')


