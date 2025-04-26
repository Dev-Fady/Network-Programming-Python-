import socket
infolist=socket.getaddrinfo(None,'smtp',socket.AF_INET,socket.SOCK_STREAM,
                            0,socket.AI_ADDRCONFIG)
info=infolist[0]
print(info[0:3])

sock=socket.socket(*info[0:3])
sock.bind(info[4])
sock.listen()
conn,add=sock.accept()

msg=input("enter msg")
msg=msg.encode('ascii')
conn.sendall(msg)

data=conn.recv(1024).decode('ascii')
print(data)

