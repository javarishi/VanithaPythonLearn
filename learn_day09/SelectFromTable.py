import learn_day09.DBConnectionUtil as util

sql_select = "select * from customers where name like %s"
vals = ("%e%",)

conn = util.get_connection()
cursor = conn.cursor()
cursor.execute(sql_select, vals)
myresult = cursor.fetchall()
print(type(myresult))
for eachrow in myresult:
    print(type(eachrow), eachrow[0], eachrow[1])

util.closeAll(cursor, conn)
