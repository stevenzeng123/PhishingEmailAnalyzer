from OTXv2 import OTXv2
import get_malicious



def verify_url(check_url, otx):
        for url in check_url:
            alerts = get_malicious.url(otx, url)
            if alerts:
                print("Potentially malicious URL:", url)
                print(alerts)
            else:
                print("URL is not identified as malicious:", url)

def verify_domain(check_domain, otx):
        alerts = get_malicious.hostname(otx, check_domain)
        if alerts:
            print("Potentially malicious domain:", check_domain)
            print(alerts)
        else:
            print("Domain is not identified as malicious:", check_domain)

def verify_ip(check_ip, otx):
        for ip in check_ip: 
            alerts = get_malicious.ip(otx, ip)
            if alerts:
                print("Potentially malicious IP:", ip)
                print(alerts)
            else:
                print("IP is not identified as malicious:", ip)

def verify_hash(hashed, otx):
        for hash in hashed:
            alerts = get_malicious.file(otx, hash)
            if alerts:
                print("Potentially malicious file:", hash)
                print(alerts)
            else:
                print("File is not identified as malicious:", hash)