import mysql.connector


def get_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="python_july_21"
    )
    return mydb


def closeAll(cursor, conn):
    cursor.close()
    conn.close()