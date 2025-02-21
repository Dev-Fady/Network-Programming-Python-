import socket
def broadcast_server(ip, port):
     #^ """ دالة تقوم بإرسال رسالة بث (Broadcast) عبر UDP ثم تستقبل الرد """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #^1- إنشاء مقبس UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  #^2- تمكين وضع البث

    #^3- ربط العنوان (IP, Port) مع السوكت
    sock.bind((ip, port))

    print("🚀 UDP Broadcast Server is running...")

    while True:
         print("⏳ Waiting for clients...")

        
         #^4- استقبال البيانات من العميل (حجم البيانات الأقصى 1024 بايت)
         received_data, client_address=sock.recvfrom(1024)

         received_data=received_data.decode('ascii')
         print(f" Received data from {client_address}: {received_data}")

         #^5- إرسال رد إلى العميل
         response = " Reply from broadcast server"
         sock.sendto(response.encode('ascii'), client_address)

# ! تشغيل السيرفر على جميع العناوين (0.0.0.0) والمنفذ 12345
broadcast_server("0.0.0.0",12345)