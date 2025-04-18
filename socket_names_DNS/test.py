import socket
# print(socket.gethostname())
# print(socket.gethostbyname('cern.ch'))

# print(socket.getaddrinfo(socket.gethostname(),'12345'))

# print(socket.gethostbyaddr('127.0.0.1'))
# print(socket.getprotobyname('UDP'))
# print( socket.getservbyname('www'))
# print(socket.getservbyport(80))

from pprint import pprint 
infolist=socket.getaddrinfo('gogle.com','www',socket.AF_INET)

pprint(infolist)

info=infolist[0]
print(info[0:3])
sok=socket.socket(*info[0:3])
print(info[4])
sok.connect(info[4])
print(sok.getsockname())