import socket,struct
header_struct=struct.Struct('!I')
def client(address):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(address)
    print('Connected to server:',sock.getsockname())

    sock.shutdown(socket.SHUT_RD)
    
    put_block(sock,b'client: Hello')
    put_block(sock,b'client: test send message ')
    put_block(sock,b'client: end')
    put_block(sock,b'')
    put_block(sock,b'test')
    sock.close()


def put_block(sock,message):
    block_length=len(message)
    sock.send(header_struct.pack(block_length))
    sock.send(message)

client(('127.0.0.1', 12346))
