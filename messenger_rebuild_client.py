import socket
import threading
from tkinter import *

HEADER = 2048
PORT = 5050
FORMAT = 'utf-8'
DC_MSG = "!DC"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def listen():
    while True:
        print(f"server: {client.recv(2048).decode(FORMAT)}" )

def inputing():
    while True:
        balls = input("")
        send(balls)


def start():
    thread = threading.Thread(target=listen)
    thread.start()
    thread2 = threading.Thread(target=inputing)
    thread2.start()

start()

