import bluetooth
import time

counter = 0

start = time.time()
#while True:
iterations = 10

port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(("9C:B1:50:1A:7B:FA", port))

while counter <= iterations: 
    sock.send("hello!!")
    sock.close()
    counter+=1
end = time.time()
elapsed = end-start
print(elapsed)
