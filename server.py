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

"""
This dispatcher takes client request from the client queue in 
FIFO way and gets back the response
""" 
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

"""
Main starts the dispatcher thread which will start serving client as they send their request. The client is added to the list(shared object done so that if we need multiple dispatcher to increase throughput) as they come.
"""

def Main(): 
    start_new_thread(dispatcher,())
    host = "" 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
  
    s.listen(5) 
    print("socket is listening")    
    while True: 
  
        c, addr = s.accept()   
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
        q_list.append([c,addr])
        print_lock.release()
    s.close()
