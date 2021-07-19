'''
https://github.com/apache/activemq/blob/main/assembly/src/release/examples/stomp/python/stomppy/listener.py
'''

import stomp
import time

host =  "localhost"
port = 61613
destination="test.queue"
messages = 100


class MyListener:

    def __init__(self, conn):
        self.conn = conn
        self.count = 0
        self.start = time.time()

    def on_error(self, message):
        print('received an error %s' % message)

    def on_message(self, message):
        if message == "SHUTDOWN":
            diff = time.time() - self.start
            print("Received %s in %f seconds" % (self.count, diff))
            conn.disconnect()
        else:
            print(message)
            print(message.headers)
            print(message.body)



conn = stomp.Connection(host_and_ports = [(host, port)])
conn.set_listener('RishizListener', MyListener(conn))
conn.connect()
conn.subscribe(destination=destination, id=1, ack='auto')
print("Waiting for messages...")
while 1:
    time.sleep(10)