import socket
from pprint import pprint
infolist = socket.getaddrinfo('kernal.org','ftp', socket.AF_INET,
                              socket.SOCK_STREAM,0,socket.AI_ADDRCONFIG |
                              socket.AI_V4MAPPED)
pprint(infolist)

info = infolist[0]
print(info[0:3])

sok = socket.socket(*info[0:3])
sok.connect(info[4])

msg = sok.recv(1024)
print(msg.decode())

sok.send('Client: hello Im client '.encode())
