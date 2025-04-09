import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345
server_add = (host, port)

client.connect(server_add)
nickName = ''

def receive_message():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                global nickName
                nickName = input("Enter your nickname: ")
                client.sendall(nickName.encode('ascii'))
            else:
                print("Server: " + message)
        except:
            print("An error occurred:")
            client.close()
            break

def SendMessage():
    while True:
        try:
            msg = input()
            client.sendall(msg.encode('ascii'))
        except:
            print("An error occurred:")
            client.close()
            break


receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

write_thread = threading.Thread(target=SendMessage)
write_thread.start()
