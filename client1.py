""" 
This is Client trying to connect with the web service and wants to see Temperature
Of Lucknow India.

NOTE: Here IP address has been taken as Locathost, however you can use your IP and use web service like Apache(Port 80)
 
"""
import socket 
import json 
import datetime 
def print_result(data):
  print "~~~~~~~~~~~~~CLIENT 1 WINDOW~~~~~~~~~~~~~~~~~~"
  for key,val in data.items():
    if 'city' in key:
      print "City:\t\t",val
    elif 'country' in key:
      print "Country:\t\t",val
    elif 'temp' in key:
      print "Curent Temp:\t\t",val-273
    elif 'temp_max' in key:
      print "Max Temp:\t\t",val-273
    elif 'temp_min' in key:
      print "Curent Temp:\t\t",val-273
  currentDT = datetime.datetime.now()
  print 'Last Updated:\t\t',currentDT.strftime('%Y-%m-%d %H:%M:%S')
  print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

def ClientMain2(): 
    while(1):
      host = '127.0.0.1'  
      port = 12345
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
      s.connect((host,port)) 
      message = "http://127.0.0.1:5000/weatherapi/Lucknow" 
      s.send(message.encode('ascii')) 
      data = s.recv(1024)       
      print_result(json.loads(data))
      #print('Received from the server :',str(data.decode('ascii'))) 
      s.close()
  
if __name__ == '__main__': 
    Main()
