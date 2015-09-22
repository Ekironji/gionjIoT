#!/usr/bin/python

import socket
import sys
import json
import getopt
import time

def printHelp():
   print 'Usage:'
   print '  argument is a number, the node: python tcp_client.py 1'

def main(argv):
   TCP_IP = '192.168.0.104'
   TCP_PORT = 10002
   BUFFER_SIZE = 1024
   		
   responseData = {"REQUEST":"JOIN","HOSTNAME":'NODE_'+str(sys.argv[1]),"SERVICES":"1dsdsds|22|33"}
   sensorData = {"REQUEST":"SENSORS_DATA","HOSTNAME":'NODE_'+str(sys.argv[1]),"LABELS":"aX|aY|aZ","VALUES":"aaa|2ddd2|33fff"}

   try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((TCP_IP, TCP_PORT))
      MESSAGE = json.dumps(responseData)
      print MESSAGE
      while 1:
         MESSAGE = json.dumps(sensorData)     
         print MESSAGE
         s.send(MESSAGE)
         data = s.recv(BUFFER_SIZE)
         time.sleep(1)
      s.close()
   except KeyboardInterrupt:		
      s.close()
      print "INTERRUZIONE"  

   print "(belzedootest.py) tcp response:", data

if __name__ == "__main__":
   main(sys.argv[1:])
