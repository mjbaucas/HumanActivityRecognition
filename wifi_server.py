import socket
import time
import sys

ip_addresses = [
    "10.12.162.178",
]

counter = 0
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5000))
    s.listen(10)
    print('Server is now running.')
    connection, address = s.accept()
    print(address)
    if address[0] == ip_addresses[counter]:
        print(f"Connection from {address} has been established.")
        message = connection.recv(1024)
        print(message)
        counter+=1
        if counter >= len(ip_addresses):
            counter = 0
    else:
        connection.recv(1024)
        connection.sendall(bytes("", "utf-8"))
        
    print(counter)
    connection.close()