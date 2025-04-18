import dns.resolver

def lookup(name):
    for RecType in 'A','AAAA','CNAME','MX','NS':
        answer=dns.resolver.query(name,RecType,raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)

lookup('google.com')