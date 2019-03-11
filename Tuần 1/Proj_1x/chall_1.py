import socket
socket.setdefaulttimeout(2)
s=socket.socket()
i=1000
target= 'attack.samsclass.info'
while i<10000:
     try:
        s.connect((target,i))
        s.send('HEAD / HTTP/1.1\nHost: '+ target +'\n\n')
        print s.recv(1024)
        s.close()
     except socket.error,v:
        print 'Port',i,'does not work'
        i=i+1000