import dns.resolver

res=dns.resolver.query('google.com', 'A')
for val in res:
    print('A Record:', val.to_text())

res=dns.resolver.query('google.com', 'AAAA')
for val in res:
    print('AAAA Record:', val.to_text())

# ! error 
# res=dns.resolver.query('google.com','CNAME')
# for val in res:
#     print('CNAME Record:', val.to_text())

res=dns.resolver.query('google.com', 'MX')
for val in res:
    print('MX Record:', val.to_text())