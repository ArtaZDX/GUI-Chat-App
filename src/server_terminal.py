import threading
import socket
import time

server = socket.socket()
server.bind(('localhost' , 12451))
server.listen(5)
con , addr = server.accept()

def send_data():
	while True:
		send = raw_input(">>")
		con.send(send)
		time.sleep(5)

def recv_data():
	while True:
		data_recv = con.recv(1024)
		print(data_recv)
		time.sleep(5)


threading.Thread(target=send_data).start()
threading.Thread(target=recv_data).start()