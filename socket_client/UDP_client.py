import socket
def Client():
    #^1- إنشاء كائن Socket باستخدام UDP (SOCK_DGRAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #~ الحصول على اسم الجهاز المحلي
    host = socket.gethostname()
    port = 12345
    server_add = (host, port)

    message = "Hello Server , I'm client"
    #^2- إرسال البيانات إلى الخادم
    sock.sendto(message.encode('ascii'), server_add)

    #^3- استقبال الرد من الخادم
    data, server = sock.recvfrom(1024)
    print("📨 Response from server:", data.decode('ascii'), server)

    sock.close()

Client()