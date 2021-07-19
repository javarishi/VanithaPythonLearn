import learn_day09.DBConnectionUtil as util

sql = "UPDATE customers SET address = %s WHERE name = %s"
val = ("Valley 345", "Peter")

conn = util.get_connection()
cursor = conn.cursor()
cursor.execute(sql, val)
conn.commit()
print(cursor.rowcount, "record(s) updated")
util.closeAll(cursor, conn)
