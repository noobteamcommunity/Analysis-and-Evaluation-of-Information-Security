import socket
import time
 
socket.setdefaulttimeout(2)
s=socket.socket()
a=socket.socket()
p=socket.socket()
i=3000
target= 'attackdirect.samsclass.info'
s.connect((target,3100))
print 'Connected to port: 3100'
while i<4000:
     a.connect((target,i))
     print 'Connected to 2nd port'
     print 'Knocking...'
     time.sleep(2)
     try:
         p.connect((target,3003))
         p.send('HEAD / HTTP/1.1\nHost: '+ target +'\n\n')
         print p.recv(1024)
         i=4000
     except socket.error,v:
         print 'Port',i,'does not work'
         i=i+100
         continue
a.close()
s.close()
p.close()