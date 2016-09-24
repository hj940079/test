#-*- coding: UTF-8 -*-
import os,sys,linecache,random,socket

ID=0
PORT=0
CLOCK=0

def get_Config(argv):
	if(len(argv)<3):
		return False
	else :
		config = linecache.getline(argv[1],int(argv[2]))
		#if find right record from file set id and port, then return true, else return false
		if(config.strip()==''):
			return False
		else:
			para=config.split(' ')
			global ID
			ID=int(para[0])
			global PORT
			PORT=int(para[1])
			return True

def get_RandomNumber(max_number):
	return int(random.random()*(max_number+1))      
# return x and 0<=x<=max_number

def local_Event():
	global CLOCK
	CLOCK+=get_RandomNumber(6)

def receieve_Message():
	#define message as 'type:(ping or clock),clock:(clock)'
	host=socket.gethostname()
	s.bind((host,port))
	s.listen(5)
	while True:
		
		if s.recv(1024)

if get_Config(sys.argv):
	print('ID:',ID,' port:',PORT)
else
	print('No right line for configuration')


'''
send message
receive message
update clock count
write result
'''



"""
1, Configuration file is basically a list of clients with different id and port for listening,
what if the number of clients is smaller then the number avalibale for configure.
Does that mean every client have to sniff around and find the active client? 
Does this also mean that client have to have a list to store the list of other clients?
2, Are the id and port in the configuration file randomly selected and in random order, or they are in certain order?
On the other hand, does client have to test if the port is occupied itself? 
3, Once we start to test the algrithm, we almost surely will start the clients one by one, 
for those who have already started, even though we make it sniff around, it still will not those clients which will start in the future. 
Does this mean client program have to keep dectecting for other new clients constantly?

"""

"""
A list for active client
Periodically ping to other clients to update the list
Mannually control the exact configuration for the new client
"""
