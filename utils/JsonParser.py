import socket
import sys
import json
import serial
import time
import traceback

INPUT = 0
OUTPUT = 1
LOW = 0
HIGH = 1

class Parser:

   ser = None
   ans = ''
    
   def printArray(self, array):
      ans = ""
      for val in array:
         ans += str(val) + " "
      return ans  

   def writeToSerial(self, dataToSend):
      print self.printArray(self.pinMode)
      print self.printArray(self.value)
      dataToSend = dataToSend.replace(" ","")      
      print "(JsonParser.writeToSerial) data to be send to SAM3X: " + dataToSend
      
      out = ''
      try:
         if input == 'exit':
            print '(JsonParser.writeToSerial) 2 '
            ser.close()
            exit()
         else:
            print '(JsonParser.writeToSerial) 2b '
            self.ser.write(dataToSend + '\r')
            out = ''
            time.sleep(0.05)
            while self.ser.inWaiting() > 0:			   
               out += self.ser.read(1)
      except:
          print(traceback.format_exc())
          print "(JsonParser) Error in send to serial"
          return ''
		   		           
      print "(JsonParser) Response from SAM3X: " + out
      return out
      
   def __init__(self):
      self.pinMode = [\
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0]
      self.value = [
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0]
      
      # configure the serial connections (the parameters differs on the device you are connecting to)
      try:
         self.ser = serial.Serial(
            port='/dev/ttymxc3',
            baudrate=115200
         )
         print "(JsonParser) Serial ttymxc3 connected at 115200" 
      except:
		  print "Serial connection fail!"
		  exit()

   def processCommand(self, data):    
      try:
         decoded = json.loads(data)
      except (ValueError, KeyError, TypeError):
         print >> sys.stderr, "(Json parser) JSON format error"
         return -1
            
      if decoded['method'] == "pinMode":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 55:
            if int(decoded['value']) == 0 or decoded['value'] == 'INPUT':
               self.pinMode[int(decoded['pin'])] = 0;
            elif int(decoded['value']) == 1 or decoded['value'] == 'OUTPUT':
               self.pinMode[int(decoded['pin'])] = 1;
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "(Json parser) Error: Invalid pin number"

      elif decoded['method'] == "digitalWrite":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 55:
            if int(decoded['value']) == 0 or decoded['value'] == 'LOW':
               self.value[int(decoded['value'])] = 0;
            elif int(decoded['value']) == 1 or decoded['value'] == 'HIGH':
               self.value[int(decoded['value'])] = 1;
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "Error: Invalid pin number"

      elif decoded['method'] == "digitalRead":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 55:         
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "(Json parser) Error: Invalid pin number"

      elif decoded['method'] == "analogWrite":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 14:
            #controllo
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "(Json parser) Error: Invalid pin number"

      elif decoded['method'] == "analogRead":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 55:         
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "Error: Invalid pin number"

      elif decoded['method'] == "map":
		 ans = self.writeToSerial(data)
         
      elif decoded['method'] == "hi":
         ans = self.writeToSerial(data)   

      else:
         print >>sys.stderr, "Error> method unkown"
      
      # SCRIVI IN SERIALE E ASPETTA IL RISULTATO      
      print "(JsonParser.parseCommand) risposta dal sam: " + ans   
      
      return ans
      

