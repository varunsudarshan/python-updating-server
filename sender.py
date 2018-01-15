import time
import random
import socket
host = "192.168.0.101" #server ip
port = 5000
sender_socket = socket.socket()
while True:
	try:
		sender_socket.connect((host,port))
	except socket.error,e:
		print e
		print "retrying"
		continue
	break
while True:
	a=random.randint(0,100)
	print "sending "+str(a)
	sender_socket.send(str(a))
	time.sleep(1)

sender_socket.close()