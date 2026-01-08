import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 5
server_sock.bind(("", port))
server_sock.listen(1)

while True:
    try:
        client_sock,address = server_sock.accept()
        print("Accepted connection from " + str(address))

        data = client_sock.recv(1024)
        if data:
            print("Received:", data.decode())
        
        client_sock.close()
    except OSError as e:
        print("Error:", e)
        
server_sock.close()