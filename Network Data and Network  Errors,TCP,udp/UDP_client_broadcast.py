import socket

def client(id,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

    text='hi server , I\'m client boradcast'
    sock.sendto(text.encode('ascii'), (id,port))

    msg,add=sock.recvfrom(1024)
    msg=msg.decode('ascii')
    print(f"Received from {add}: {msg}") 

client("<broadcast>",12345)