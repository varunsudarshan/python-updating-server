import time
import random
import socket
host = socket.gethostname();
port = 5000
sender_socket = socket.socket()
sender_socket.connect((host,port))
while True:
	a=random.randint(0,100)
	print "sending "+str(a)
	sender_socket.send(str(a))
	time.sleep(1)

sender_socket.close()