import socket
import threading
import time
from Tkinter import *


client = socket.socket()
client.connect(('localhost' , 63453))
root = Tk()


def send():
	data_send = get_message.get()
	if data_send != "":
		data_send = str(data_send)
		client.send(data_send)
		lbl = Label(root , text=data_send , bg="red" , fg="white")
		get_message.delete(0 , END)
		lbl.pack(fill=X , side=TOP)

def recv():
	while True:
		data_recv = client.recv(1024)
		if data_recv != "":
			lbl = Label(root , text=data_recv , bg="blue" , fg="white")
			lbl.pack(fill=X , side=TOP)


get_message = Entry(root)
send_message = Button(root , text="Send" , command=send)

send_message.pack(fill=X , side=BOTTOM)
get_message.pack(fill=X , side=BOTTOM)

threading.Thread(target=recv).start()


root.title("Chat Client")
root.geometry("500x700")
root.resizable(width=False , height=False)

root.mainloop()