import socket              
import _thread
import time

def reply(addr,c):
	
	print('get connection from',addr)
	str='Thank you for connecting'
	c.send(bytes(str, 'UTF-8'))
	time.sleep(0.01)
	count=0
	while count<5:
		count+=1
		c.send(bytes('Hello '+time.ctime(), 'UTF-8'))
		time.sleep(3)
	c.close()

s = socket.socket()       
host = socket.gethostname() 
port = 12345               
s.bind((host, port))       
s.listen(5)                 
while True:
	c, addr = s.accept()
	if len(addr)!=0:
		 _thread.start_new_thread( reply, (addr, c, ) )
