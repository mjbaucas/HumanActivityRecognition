import socket
import time 

reset = 1
start = 0
iterations = 100000
counter = 0

start = time.time()
#while True:
while counter <= iterations:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.11.217.162", 5000))
        s.sendall(bytes('Hello.', "utf-8"))
        message = s.recv(1024).decode("utf-8")
        counter+=1
        print(counter)
        s.close()
    except Exception as msg:
        print(msg)
        reset = 0
end = time.time()
elapsed = end-start
print(elapsed)
if elapsed > 1.0:
    print(elapsed)
