import socket
import struct

# تعريف شكل الهيدر (طوله 4 بايت - unsigned int)
header_struct = struct.Struct('!I')

def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)  

    print('Listening on', sock.getsockname())
    conn, addr = sock.accept() 
    print('Accepted connection from', addr)

    conn.shutdown(socket.SHUT_WR)

    # استقبال البيانات في صورة كتل blocks
    while True:
        block = get_block(conn)
        if not block:
            break
        print('Block Says:', repr(block))

    conn.close()
    sock.close()

def get_block(sock):
    # قراءة طول البيانات (الهيدر)
    data = sock.recv(header_struct.size)
    (block_length,) = header_struct.unpack(data)  # تحويل البايت لطول البلوك
    return recvall(sock, block_length)

def recvall(sock, length):
    # استلام البيانات كاملة حسب الطول المطلوب
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise
        data += more
    return data.decode()

server(('127.0.0.1', 12346))
