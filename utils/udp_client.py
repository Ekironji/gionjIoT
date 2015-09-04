#!/usr/bin/python

import socket
import sys
import json
import getopt


def main(argv):
	UDP_IP = "127.0.0.1"
	UDP_PORT = 10001
	
	sendData = {'request':'whois','key':123456}
	sendDataString = json.dumps(sendData)	

	print "UDP target IP:", UDP_IP
	print "UDP target port:", UDP_PORT
	print "message:", sendData

	sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    # broadcast configuration                  
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	
	# request send
	sock.sendto(sendDataString, ('255.255.255.255', UDP_PORT))
	
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	
	## decodifico col json
	decodedJson = json.loads(data)
	
	if decodedJson['response'] == 'true':
		print 'ip_address' + decodedJson['ip_address']
	
	exit
    
if __name__ == "__main__":
	main(sys.argv[1:])
