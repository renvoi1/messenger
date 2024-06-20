import socket
import threading

HEADER = 2048
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DC_MSG = "!DC"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"user conn. at {addr}")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DC_MSG:
                connected = False
            print(f"{addr} said {msg}")
            # balls = input("MESSAGE: ")
            # conn.send(balls.encode(FORMAT))

    conn.close()
def start():
    server.listen()
    print(f"listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args =(conn, addr))
        thread.start()
        #print(f"actv conn. {threading.activeCount() - 1}")


print("chat online")
start()