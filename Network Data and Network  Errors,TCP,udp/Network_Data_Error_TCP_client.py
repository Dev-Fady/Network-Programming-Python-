import socket, struct
header_struct = struct.Struct('!I')
class desError(Exception):
    def __str__(self):
        return '%s: %s'%(self.args[0], self.__cause__.strerror)
try:
    def client():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        host = socket.gethostname()
        port=1133
        add=('host',port)
        try:
          sock.connect(add)
        except socket.gaierror as e:
            print(e.errno)
            print(e.strerror)
            raise desError('error description ') from e
        sock.shutdown(socket.SHUT_RD)
        put_bloc(sock, b'hi im client ')
        put_bloc(sock, b'hi im client1 ')
        put_bloc(sock, b'hi im 1234 ')
        put_bloc(sock, b'')
        sock.close()
except (socket.gaierror, socket.timeout, socket.error) as e:
    print(e.errno)
    print(e.strerror)
    raise desError('error description ') from e

def put_bloc(sock,mess):
    block_length=len(mess)
    sock.send(header_struct.pack(block_length))
    sock.send(mess)

host=socket.gethostname()
client()