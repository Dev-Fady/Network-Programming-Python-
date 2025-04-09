import threading
import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port=12345
server_add=(host, port)

sock.bind(server_add)
sock.listen()

clients = []
nicknames = []

def handle():
    while True:
        client, addr = sock.accept()
        print(f"Connected with {addr}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")

        clients.append(client)
        nicknames.append(nickname)

        print(f"Nickname: {nickname}")
        broadcast(f"{nickname} joined the chat room")

        thread = threading.Thread(target=receive, args=(client,))
        thread.start()


def broadcast(msg):
    for client in clients:
        try:
            client.send(msg.encode("ascii"))
        except:
            client.close()
            clients.remove(client)

def receive(client):
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            index = clients.index(client)
            nickname = nicknames[index]
            broadcast(f"{nickname}: {msg}")
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            clients.remove(client)
            nicknames.remove(nickname)
            client.close()
            broadcast(f"{nickname} left the chat room")
            break

handle()