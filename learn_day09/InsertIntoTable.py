import learn_day09.DBConnectionUtil as util

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
vals = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Viola', 'Sideway 1633')
]


conn = util.get_connection()
cursor = conn.cursor()
# cursor.execute(sql, val)
cursor.executemany(sql, vals)
conn.commit()
util.closeAll(cursor, conn)

