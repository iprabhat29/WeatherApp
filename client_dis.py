import threading
import thread

from client import *

from client1 import *

from client2 import *

if __name__ == '__main__':
  t = threading.Thread(target=ClientMain, args=())
  t1 = threading.Thread(target=Client1Main, args=())
  t2 = threading.Thread(target=Client2Main, args=())
  t.start()
  t1.start()
  t2.start()
