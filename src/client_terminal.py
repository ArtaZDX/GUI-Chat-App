import threading
import socket

client = socket.socket()
client.connect(('localhost' , 12451))

def recv():
	while True:
		data_get = client.recv(1024)
		print(data_get)

def send():
	while True:
		text = raw_input(">>")
		client.send(text)

threading.Thread(target=send).start()
threading.Thread(target=recv).start()