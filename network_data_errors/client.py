import socket
soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12345

serv_addr=(host,port)
soc.connect(serv_addr)
print('Connected to server:', serv_addr)
soc.shutdown(socket.SHUT_RD)
soc.sendall('client: Hello'.encode())
soc.sendall('client: test send message '.encode())
soc.sendall('client: end'.encode())
print('Sent all data')