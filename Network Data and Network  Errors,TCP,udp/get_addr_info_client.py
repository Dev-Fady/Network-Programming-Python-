import socket
infolist=socket.getaddrinfo(None,'smtp',socket.AF_INET,socket.SOCK_STREAM,
                            0,socket.AI_ADDRCONFIG)
info=infolist[0]
print(info[0:3])

sock=socket.socket(*info[0:3])
sock.connect(info[4])

msg=sock.recv(1024).decode('ascii')
print(msg)

data=input("enter msg")
data=data.encode('ascii')
sock.sendall(data)