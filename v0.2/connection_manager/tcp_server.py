import socket
import sys
import json
import traceback

from JsonParser import Parser

TCP_PORT = 10000 

def main(argv):
	# Init parser obj
	core = Parser()

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = ('', TCP_PORT)
	print >> sys.stderr, '(TCPServer.py) starting up on %s port %s' % server_address
	sock.bind(('', TCP_PORT))

	# Listen for incoming connections
	sock.listen(1)

	ans = ''

	while True:
		# Wait for a connection
		print >> sys.stderr, '(TCPServer.py) waiting for a connection'
		connection, client_address = sock.accept()
		try:
			print >>sys.stderr, '(TCPServer.py) connection from', client_address

			# Receive the data in small chunks and retransmit it
			while True:
				incoming_data = connection.recv(1024)
				print >>sys.stderr, '(TCPServer.py) received string from tcp client "%s"' % incoming_data
				# se ci sono dati li processo
				if incoming_data:
					try:
						# chiamo il parser json 
						ans = core.processCommand(incoming_data) 

					except (ValueError, KeyError, TypeError):
						print >> sys.stderr, "(TCPServer.py) JSON format error"
					
					print '(TCPServer.py) sending data back to the client'
					connection.sendall(ans)
				else:
					print >>sys.stderr, '(TCPServer.py) no more data from', client_address
					break
		except KeyboardInterrupt:		
			connection.close()
			print "(TCPServer.py) Interruzione da tastiera gestita"
		finally:
			# Clean up the connection
			connection.close()



def printHelp():
   print 'Usage:'



def startConnection(netId, deviceAlias):
   print 'startConnection called'
	
def getStatus():
   print 'getStatus called'

def getAvailableServices():
   print 'getAvailableServices called'
	
def getServiceDescription(serviceType):
   print 'getServiceDescription called'

def getActiveServices():
   print 'getActiveServices called'
   

def addService(serviceType, serviceSubType, params):
   print 'addService called'
	
def setService(serviceId, params):
   print 'setService called'
	
def deleteService():
   print 'deleteService called'
	
	
def getActiveConnections():
   print 'getActiveConnections called'
	
def setConnections(src_addr, src_sevice_id, dst_addrdst_service):
   print 'setConnections called'
	
def deleteConnections(connectionId):
   print 'deleteConnections called'
	

if __name__ == "__main__":
   main(sys.argv[1:])
