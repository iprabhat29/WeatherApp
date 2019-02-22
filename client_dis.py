import threading
import thread

from client import *

from client1 import *

from client2 import *

if __name__ == '__main__':
  t = threading.Thread(target=ClientMain1, args=())
  t1 = threading.Thread(target=ClientMain2, args=())
  t2 = threading.Thread(target=ClientMain3, args=())
  t.start()
  t1.start()
  t2.start()
