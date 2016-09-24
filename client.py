import socket            
import time


s = socket.socket()         
host = socket.gethostname() 
port = 12345                
s.connect((host, port))
p = time.time()
while time.time()-p<5:
	str=s.recv(1024)
	if(len(str)!=0):
		print(str)
		p=time.time()
s.close                
