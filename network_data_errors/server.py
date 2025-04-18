import socket
soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12345

soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

soc.bind((host,port))
soc.listen()

conn,add=soc.accept()
conn.shutdown(socket.SHUT_WR)

msg=b''
while True:
    data=conn.recv(4)
    if not data:
        print('No  more data')
        break
    print(data)
    msg+=data

print(msg.decode())