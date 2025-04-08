import socket
print(socket.gethostname())
print(socket.gethostbyname('cern.ch'))

# print(socket.getaddrinfo())

print(socket.gethostbyaddr('127.0.0.1'))
print(socket.getprotobyname('UDP'))
print( socket.getservbyname('www'))
print(socket.getservbyport(80))