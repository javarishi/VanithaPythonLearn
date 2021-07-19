import learn_day09.DBConnectionUtil as util

sql_query = "create database python_july_21"

conn = util.get_connection()
cursor = conn.cursor()
cursor.execute(sql_query)
print("Scema created")
util.closeAll(cursor, conn)
