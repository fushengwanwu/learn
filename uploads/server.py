#coding:utf-8
from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('',6666))
s.listen(1)
sock,addr = s.accept()
print 'Connected by ',addr
sock.send('Welcome to iChunqiu')
text = sock.recv(1024)
sock.close
s.close()