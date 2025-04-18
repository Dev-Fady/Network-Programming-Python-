import dns.resolver

def resolve_mail(domin):
    answer=dns.resolver.query(domin,'MX',raise_on_no_answer=False)
    if answer.rrset:
        records=sorted(answer)
        print('record after sorting')
        print(records)
        for record in records:
            print(record.exchange)
            name=record.exchange.to_text(omit_final_dot=True)
            print(name)
            resolve_host(name)
        else:
            print('No MX records found for the domain.')
            resolve_host(domin)
            return

def resolve_host(host):
    answer=dns.resolver.query(host,'A',raise_on_no_answer=False)
    if answer.rrset is not None:
        for record in answer:
            print('hostname :',host,'has address:',record.address)
        return
    else:
        answer=dns.resolver.query(host,'AAAA',raise_on_no_answer=False)
    if answer.rrset is not None:
        for record in answer:
            print('hostname :',host,'has address:',record.address)
        return
    else:
        answer=dns.resolver.query(host,'CNAME',raise_on_no_answer=False)
        if answer.rrset is not None:
            record=answer[0]
            cname=record.address
            resolve_host(record.address)
        else:
            print('error no a,AAAA or CNAME for host name ')

resolve_mail('gmail.com')
