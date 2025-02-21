import socket  
def client(ip, port):
    #^ """ دالة تقوم بإرسال رسالة بث (Broadcast) عبر UDP ثم تستقبل الرد """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #^1- إنشاء مقبس UDP
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  #^2- تمكين وضع البث

    text = 'Broadcast datagram!'
    sock.sendto(text.encode('ascii'), (ip, port))  #^3- إرسال الرسالة

    msg, add = sock.recvfrom(1024)  #^4- انتظار الرد
    msg = msg.decode('ascii')  # فك تشفير الرسالة
    print(f"Received from {add}: {msg}")  # طباعة النتيجة

client("<broadcast>", 12345)