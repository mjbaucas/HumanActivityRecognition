import bluetooth
import time

counter = 0

start = time.time()
iterations = 10
port = 1

while counter <= iterations: 
    try:
        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect(("9C:B1:50:1A:7B:FA", port))
        message = "hello!!"
        sock.send(message.encode())
        sock.close()
        counter+=1
    except OSError as e:
        print("Connection failed:", e)
        
end = time.time()
elapsed = end-start
print(elapsed)
