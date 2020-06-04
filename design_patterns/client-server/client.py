import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2404))
received = (client.recv(1024)).decode()
print("Received: {0}".format(received))
client.close()