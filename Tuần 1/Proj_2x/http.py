import socket
s=socket.socket()

req = """POST /python/login2.php HTTP/1.1

Host: attackdirect.samsclass.info

Connection: keep-alive

Content-Length: 7

Cache-Control: max-age=0

Origin: null

Upgrade-Insecure-Requests: 1

DNT: 1

Content-Type: application/x-www-form-urlencoded

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8

Accept-Encoding: gzip, deflate

Accept-Language: en-GB,en;q=0.9,en-US;q=0.8,vi;q=0.7

Cookie: __cfduid=dd151b2c7a55c47c90ab51c399222fed31552008466



u=a&p=b"""

s.connect(("attackdirect.samsclass.info",80))
s.send(req)
print s.recv(1024)
s.close()