import learn_day09.DBConnectionUtil as util

sql_create = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"

conn = util.get_connection()
cursor = conn.cursor()
cursor.execute(sql_create)
util.closeAll(cursor, conn)
