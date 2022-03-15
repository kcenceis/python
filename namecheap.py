import requests

##namecheap API##
#https://www.namecheap.com/support/knowledgebase/article.aspx/29/11/how-to-dynamically-update-the-hosts-ip-with-an-http-request/
##


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
