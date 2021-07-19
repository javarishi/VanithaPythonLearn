import learn_day09.DBConnectionUtil as util

sql = "DELETE FROM customers WHERE address = %s"
vals = ('Mountain 21',)
conn = util.get_connection()
cursor = conn.cursor()
cursor.execute(sql, vals)
conn.commit()
print(cursor.rowcount, "record(s) deleted")
util.closeAll(cursor, conn)

