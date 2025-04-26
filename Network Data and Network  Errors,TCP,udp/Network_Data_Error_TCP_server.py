import socket,struct
header_struct=struct.Struct('!I')
class desError(Exception):
    def __str__(self):
        return '%s: %s'%(self.args[0], self.__cause__.strerror)
try:
    def server(address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind(address)
        except socket.gaierror as e:
            print(e.errno)
            print(e.strerror)
            raise desError('error description ') from e
        sock.listen()
        print('Listening at ', sock.getsockname())
        sock.settimeout(10)
        conn, add = sock.accept()
        conn.shutdown(socket.SHUT_WR)
        while True:
            bloc = get_bloc(conn)
            if not bloc:
                break
            print('Bloc says', repr(bloc))
        conn.close()
        sock.close()
except (socket.gaierror, socket.timeout,socket.error) as e:
    print(e.errno)
    print(e.strerror)
    raise


def get_bloc(sock):
    data=sock.recv(header_struct.size)
    (bloc_length,)=header_struct.unpack(data)
    return recvall(sock,bloc_length)

def recvall(sock,length):
    data=''
    while len(data) < length:
        more = sock.recv(length -len(data)).decode('ascii')
        print(data)
        if not more:
            raise
        data+=more
    return data

host=socket.gethostname()
server(('host',1133))