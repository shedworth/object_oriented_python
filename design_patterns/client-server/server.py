import socket
import gzip
from io import BytesIO

"""Decorator class replicating the send and close methods
of the standard Python socket interface, adding a print 
statement before sending data"""
class LogSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print(
            "Sending {0} to {1}".format(
                data, self.socket.getpeername()[0]
            )
        )
        self.socket.send(data)

    def close(self):
        self.socket.close()


class GzipSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()


"""Gets user input and sends to socket"""
def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, "utf8"))
    client.close()



compress_hosts = ['127.0.0.1']
log_send = True
"""Create server"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 240))
server.listen(1)
"""Wait for client connection then run respond function"""
try:
    while True:
        client, addr = server.accept()
        if log_send:
            client = LogSocket(client)
        if client.getpeername()[0] in compress_hosts:
            client = GzipSocket(client)
        respond(client)
finally:
    server.close()