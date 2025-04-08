import socket 
serv_sok=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=12345

server_add=(host, port)

serv_sok.bind(server_add)
serv_sok.listen()
print(serv_sok.getsockname())
print("waiting for client")
conn, addr=serv_sok.accept()
#! print(serv_sok.getpeername())
