import socket 
serv_sok=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=12345

server_add=(host, port)

serv_sok.connect(server_add)

print("client add",serv_sok.getsockname())
print("client add",serv_sok.getpeername())