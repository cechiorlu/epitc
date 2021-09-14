import mysql.connector
from mysql.connector import errors


def get_data(query):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='calc_data',
                                            user="epitc test",
                                            password='epitc')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(query)
            record = cursor.fetchone()
            print(record)

    except Error as a:
        print("Error while connecting to MySQL ", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

