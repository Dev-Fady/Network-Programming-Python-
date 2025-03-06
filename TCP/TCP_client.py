import socket  
# ! error
# def recvall(sock, length):
#   data = b''
#   while len(data) < length:
#     more = sock.recv(length - len(data))
#     if not more:
#         raise EOFError('was expecting %d bytes but only received'' %d bytes before the socket closed'% (length, len(data)))
#         data += more
#     return data

def client(host, port):
    #^ 1️⃣ إنشاء مقبس (Socket) باستخدام IPv4 و TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    #^ 2️⃣ الاتصال بالخادم
    sock.connect((host, port))  
    print("Connecting to %s port %s" % (host, port))  

    #~ 3️⃣ إرسال رسالة إلى الخادم
    sock.sendall(b'HI there, server')  

    #~ 4️⃣ استقبال الرد من الخادم
    # reply = recvall(sock, 16)
    # # Receive data
    reply = sock.recv(1024)  
    print('The server said:', reply.decode())  

    sock.close()  

client(socket.gethostname(), 2456)