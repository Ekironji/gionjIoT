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
	sock.sendto(sendDataString, (UDP_IP, UDP_PORT))
	
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
	
	## decodifico col json
	decodedJson = json.loads(data)
	
	print 'ip_address' + decodedJson['ip_address']
	
	exit
    
if __name__ == "__main__":
	main(sys.argv[1:])
