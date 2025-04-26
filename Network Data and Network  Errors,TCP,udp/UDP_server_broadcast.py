import socket 

def server(ip,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

    sock.bind((ip,port))
    print("UDP Broadcast Server is running...")

    while True:
        print("Waiting for clients...")

        msg,add=sock.recvfrom(1024)
        msg=msg.decode('ascii')
        print(f"Received data from {add}: {msg}",add[0],add[1])

        response=input("Enter your message to client: ")
        sock.sendto(response.encode('ascii'),add)

server('0.0.0.0',12345)
