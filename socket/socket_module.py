import socket

#* S = socket.socket(socket_family, socket_type, protocol=0)
# شرح المعاملات:

#* socket_family:
#~ AF_INET → لاستخدام IPv4 (الأكثر شيوعًا).
#~ AF_UNIX → للاتصال بين العمليات داخل نفس الجهاز (لن نتحدث عنه هنا).

#* socket_type:
#~ SOCK_STREAM → لإنشاء اتصال باستخدام TCP (يضمن ترتيب البيانات ووصولها).
#~ SOCK_DGRAM → لإنشاء اتصال باستخدام UDP (لا يضمن ترتيب البيانات أو وصولها).

#* protocol:
#~ يتم تركه عادةً بالقيمة الافتراضية 0، حيث يتم تحديده تلقائيًا بناءً على نوع البروتوكول المختار.


server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

hostname=socket.gethostname()
print("Hostname:", hostname)

ip_address=socket.gethostbyname(hostname)
print("IP Address:", ip_address)

ip_address_google = socket.gethostbyname("google.com")
print("Google IP Address:", ip_address_google)
print('The IP address of {} is {}'.format("google.com", ip_address_google))

port_http=socket.getservbyname("http")
print("HTTP Port:", port_http)
port_domain=socket.getservbyname("domain")
print("Domain Name Port:", port_domain)

service_53=socket.getservbyport(53)
print("53 Name Server Port:", service_53)
server_http=socket.getservbyport(80)
print("HTTP Server Port:", server_http)

