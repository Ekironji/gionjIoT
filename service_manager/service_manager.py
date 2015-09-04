import socket
import serial
import struct
import fcntl
import json


#  Services 

	## Sensors

	## Storage

	## Logic

	## Output

		### Local

		### Cloud



def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])


def main(argv):
	
	# create UDP socket
	try:
		UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		print 'Socket created'
	except socket.error, msg:
		print 'Failed to create socket. Error code: ' + str(msg[0]) + ' - Message: ' + msg[1]
		sys.exit()    

	# Bind UDP
	try:
		UDPSock.bind(("", 10001))
	except socket.error, msg:
		print 'Bind failed. Error code: ' +    str(msg[0]) + ' - Message: ' + msg[1]
		
	print 'Socket bind complete'

	# getting my ip address
	local_ip = socket.inet_ntoa(fcntl.ioctl(UDPSock.fileno(),0x8915, struct.pack('256s',"eth0"[:15]))[20:24])
	print 'IP address of this server: ' + local_ip


	while True:
		try:
			responseData = ''
			
			# recieve data from clients
			data, clientAddress = UDPSock.recvfrom(1024)
			
			# vecchio print data
			print data, ' ', clientAddress[0], '  bytes: ', ord(data[3]), ' ', ord(data[2]), ' ', ord(data[1]), ' ', ord(data[0])
			
			# spacchetto il json
			try:
				decodedJson = json.loads(data)
			except (ValueError, KeyError, TypeError):
				print >> sys.stderr, "(Json parser) JSON format error"
			
			# copio il contenuto della richiesta in variabili locali
			request = decodedJson['request']
			key = decodedJson['key']
			
			################### controllo il contenuto del messaggio: request, key

			if request == "whois":
				responseData = {'response':'true','name':'udoo-'+getHwAddr('eth0'),'ip_address':local_ip,'service_available':'','key':key}
			else:
				responseData = {'response':'false','key':key}
				
			###################	
			
			# pack response
			responseDataString = json.dumps(responseData)	
			
			# invio risposta indietro
			UDPSock.sendto(responseDataString, clientAddress)
				
		except KeyboardInterrupt:
			UDPSock.close()
			print 'Exit with keyboard output'
			
if __name__ == "__main__":
	main(sys.argv[1:])
