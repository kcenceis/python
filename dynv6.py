import requests


def getIPv4Address():
    text = requests.get('http://ipv4.ddnspod.com').text
    return text.replace("\n","").replace(" ","")


def getIPv6Address():
    text = requests.get('http://ipv6.ddnspod.com').text
    return text.replace("\n","").replace(" ","")


session = requests.session()
Update_URL = "http://dynv6.com/api/update"
domain = "" # domain
Benutzername = "" # Benutzername
your_ip = getIPv4Address()
your_ip_ipv6 = getIPv6Address()

# update ipv4 ddns
session.get(Update_URL, params={
    "hostname": domain,
    "token": Benutzername,
    "ipv4": your_ip
})
# update ipv6 ddns
session.get(Update_URL, params={
    "hostname": domain,
    "token": Benutzername,
    "ipv6": your_ip_ipv6,
    "ipv6prefix": your_ip_ipv6
})
