import socket
sok=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# try:
#     sok.connect(('nonex',80))
# except socket.gaierror as e:
#     print(e.errno)
#     print(e.strerror)
#     raise
# --------------------------------------------

serv_add=('127.0.0.1',12345)

sok.settimeout(10)
try:
    sok.connect(serv_add)
    sok.send("Hello".encode())
    msg=sok.recv(1024)
except socket.timeout as e:
    raise RuntimeError('message not recived yet')