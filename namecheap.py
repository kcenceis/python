import requests


def getIPv4Address():
    text = requests.get('http://ipv4.ddnspod.com').text
    return text.replace("\n", "").replace(" ", "")


session = requests.session()
host = ""
domain = ""
ddns_password = ""
your_ip = getIPv4Address()
session.get(url="https://dynamicdns.park-your-domain.com/update", params={
    "host": host,
    "domain": domain,
    "password": ddns_password,
    "ip": your_ip
})
