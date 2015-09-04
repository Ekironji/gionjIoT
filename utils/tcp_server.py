import socket
import sys
import json
import traceback

from JsonParser import Parser

# Init parser obj
core = Parser()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('', 10000)
print >>sys.stderr, '(TCPServer.py) starting up on %s port %s' % server_address
sock.bind(('', 10000))

# Listen for incoming connections
sock.listen(1)

ans = ''

while True:
    # Wait for a connection
    print >>sys.stderr, '(TCPServer.py) waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, '(TCPServer.py) connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            incoming_data = connection.recv(128)
            print >>sys.stderr, '(TCPServer.py) received string from tcp client "%s"' % incoming_data
            if incoming_data:
				try:
					ans = core.processCommand(incoming_data) 

				except (ValueError, KeyError, TypeError):
					print(traceback.format_exc())
					print >> sys.stderr, "(TCPServer.py) JSON format error"
                
				print '(TCPServer.py) sending data back to the client'
				connection.sendall(ans)
            else:
                print >>sys.stderr, '(TCPServer.py) no more data from', client_address
                break
    except KeyboardInterrupt:		
        connection.close()
        print "(TCPServer.py) INTERRUZIONE"
    finally:
        # Clean up the connection
        connection.close()
