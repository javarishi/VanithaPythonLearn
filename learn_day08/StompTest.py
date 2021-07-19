import stomp

host =  "localhost"
port = 61613
destination = "/topic/event"
messages = 100
data = "Hello World from Python"

conn = stomp.Connection(host_and_ports = [(host, port)])

conn.connect()

for i in range(0, messages):
    conn.send(destination="test.queue", body=data, persistent='true')

conn.send(destination=destination, body="SHUTDOWN", persistent='true')

conn.disconnect()