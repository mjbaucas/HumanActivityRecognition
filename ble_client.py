import bluetooth
import time

counter = 0

start = time.time()
#while True:
while counter <= iterations: 
    port = 1
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((targetBluetoothMacAddress, port))
    sock.send("hello!!")
    sock.close()
    counter+=1
end = time.time()
elapsed = end-start
print(elapsed)