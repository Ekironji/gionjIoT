#!/usr/bin/python

import socket
import sys
import json
import getopt

def printHelp():
   print 'Usage:'
   print '  test.py -m [ pinMode | digitalWrite | analogWrite ] -p <pin_number> -v <value>'
   print '  test.py -m [ hi | disconnect ]'
   print '  test.py -m delay -v <millis>'
   print '  test.py -m analogRead -p <pin_number>'

def main(argv):
   TCP_IP = '127.0.0.1'
   TCP_PORT = 10000
   BUFFER_SIZE = 1024
   		
   command = ''
   method = ''
   sensor = ''      
   pin = ''
   value = ''
   
   data = ''
   data_string = '' 

   # prendo i dati da i parametri
   try:
      opts, args = getopt.getopt(argv,"ha:m:s:p:v:",["address=","method=","sensor=","pin=","value="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         printHelp()
         sys.exit()
      elif opt in ("-a", "--address"):
         TCP_IP = arg
      elif opt in ("-m", "--method"):
         method = arg
         command = 'method'
      elif opt in ("-p", "--pin"):
         pin = arg
      elif opt in ("-v", "--value"):
         value = arg
      elif opt in ("-s", "--sensor"):
         sensor = arg
         command = 'sensor'
         
 
   # connect client   
   MESSAGE = 'messaggio'
   try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((TCP_IP, TCP_PORT))
      s.send(MESSAGE)
      data = s.recv(BUFFER_SIZE)
      s.close()
   except KeyboardInterrupt:		
      s.close()
      print "INTERRUZIONE"  

   print "(belzedootest.py) tcp response:", data

if __name__ == "__main__":
   main(sys.argv[1:])
