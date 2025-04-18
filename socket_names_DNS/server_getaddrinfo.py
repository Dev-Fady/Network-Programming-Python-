import socket
from pprint import pprint

infolist = socket.getaddrinfo(None, 'smtp', socket.AF_INET)
pprint(infolist)

info = infolist[0]
print(info[0:3])

sok = socket.socket(*info[0:3])
sok.bind(info[4])
sok.listen()

conn, add = sok.accept()
conn.sendall('hello Im server  '.encode())

msg = conn.recv(1024)
print(msg.decode())
