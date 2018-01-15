import socket

host = socket.gethostname()
port = 5000
rec_socket = socket.socket()

rec_socket.bind((host,port))
rec_socket.listen(2);
conn,addr = rec_socket.accept()
while True:
	data = conn.recv(1024).decode()
	print data
rec_socket.close()