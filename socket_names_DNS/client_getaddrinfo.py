import socket
from pprint import pprint

infolist = socket.getaddrinfo(None, 'smtp', socket.AF_INET)
pprint(infolist)

info = infolist[0]
print(info[0:3])

sok = socket.socket(*info[0:3])
sok.connect(info[4])

msg = sok.recv(1024)
print(msg.decode())

sok.send('Client: hello Im client '.encode())
