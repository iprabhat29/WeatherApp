import socket 
  
  
def Client2Main(): 
    # local host IP '127.0.0.1' 
    while(1):
      host = '127.0.0.1'
  
    # Define the port on which you want to connect 
      port = 12345
  
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    # connect to server on local computer 
      s.connect((host,port)) 
  
    # message you send to server 
      message = "http://127.0.0.1:5000/weatherapi/Lucknow" 
  
    #loc = raw_input('City Name : ')
        # message sent to server
    #message = message + loc 
      s.send(message.encode('ascii')) 
  
        # messaga received from server 
      data = s.recv(1024) 
  
        # print the received message 
        # here it would be a reverse of sent message 
      print('Received from the server :',str(data.decode('ascii'))) 
  
        # ask the client whether he wants to continue 
        #ans = raw_input('\nDo you want to continue(y/n) :') 
      s.close()
    # close the connection 
    #s.close() 
  
if __name__ == '__main__': 
    Main()
