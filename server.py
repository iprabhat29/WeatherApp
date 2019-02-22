# import socket programming library 
import socket 
  
# import thread module 
from thread import *
import threading 
import requests
print_lock = threading.Lock() 
from restapi import *
q_list = list()
# thread fuction 
def threaded(c):  
    while(1):
      data = c.recv(1024) 
      if not data:
        print('Bye')  
        break
      response = requests.get(data,timeout = 5)
      data_string = json.dumps(response.json())
      c.send(data_string)   
    # connection closed 
      #c.close() 
  
def dispatcher():
  while(1):
    print_lock.acquire()
    if(len(q_list)>0):
      #print ("Connected to -->",q_list.pop(0))
      threaded(q_list.pop(0)[0])
      print_lock.release()
    else:
      print_lock.release()
      continue


def Main(): 
    start_new_thread(dispatcher,())
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
    
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept()   
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
        q_list.append([c,addr])
        print_lock.release()
        # Start a new thread and return its identifier 
        #start_new_thread(threaded, (c,)) 
    s.close() 

#def run_test():
  #print "Starting REST API Backend"
  #rest_api_run()

#if __name__ == '__main__': 
    #start_new_thread(run_test,())
    #Main()
