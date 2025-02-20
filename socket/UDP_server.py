import socket

def Server():
    #^1- إنشاء كائن Socket باستخدام UDP (SOCK_DGRAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #~ الحصول على اسم الجهاز المحلي
    host = socket.gethostname()
    port = 12345
    server_add = (host, port)

    #^2- ربط العنوان (IP, Port) مع السوكت
    sock.bind(server_add)

    print("🚀 UDP Server is running...")

    while True:
        print("⏳ Waiting for clients...")

        #^3- استقبال البيانات من العميل (حجم البيانات الأقصى 1024 بايت)
        received_data, client_address = sock.recvfrom(1024)

        #^4- تحويل البيانات المستقبلة من bytes إلى string
        decoded_message = received_data.decode('ascii')
        print(f"📩 Received data from {client_address}: {decoded_message}")


        #^5- إرسال رد إلى العميل
        response = " Reply from server"
        sock.sendto(response.encode('ascii'), client_address)

#^6- تشغيل الخادم
Server()
