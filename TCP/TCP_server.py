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
def server(host, port):
    #^  1️⃣ إنشاء مقبس (Socket) باستخدام IPv4 و TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #^ 2️⃣ السماح بإعادة استخدام المنفذ بعد الإغلاق
    
    sock.bind((host, port)) #~ 3️⃣ ربط الخادم بعنوان IP ومنفذ محدد

    #~ 4️⃣ بدء الاستماع لطلبات الاتصال (بحد أقصى اتصال واحد في قائمة الانتظار)
    sock.listen(1)
    
    print("Listening at", sock.getsockname())  
    
    while True:  
        conn, sockname = sock.accept()  #~5️⃣ انتظار اتصال من عميل
        print("We have accepted a connection from", sockname)
        print(' Socket name:', conn.getsockname())
        print(' Socket peer:', conn.getpeername())
        

        # message = recvall(conn, 25)
        # print(' Incoming sixteen-octet message:', repr(message))

        message = conn.recv(1024)  #~6️⃣ استقبال البيانات من العميل
        print("data recieved from client=: ", message.decode())  

        conn.sendall('FareWell, client:'.encode())  #& 7️⃣ إرسال رد للعميل
        conn.close()  #~ إغلاق الاتصال
        
        print("Connection closed")  

server(socket.gethostname(), 2456)  # تشغيل الخادم على الجهاز المحلي
