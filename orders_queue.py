from collections import deque
import threading
import time

class OrdersQueue:
    def __init__(self):
        self.buffer = deque()

      
        

    def enque_(self,value):
        self.buffer.appendleft(value)

    def deque_(self):
        if len(self.buffer)==0:
             print("orders are empty")
        else:
            return self.buffer.pop()
            
        
    def size(self):
        return len(self.buffer)
    
    def is_not_empty(self):
        if len(self.buffer)!=0:
            return True
        else:
            return False
    def size(self):
        return len(self.buffer)
    
q = OrdersQueue()    
        
def place_orders(orders):
    
    for i in orders:
         print("order for ", i)
         q.enque_(i)
         time.sleep(0.5)

def serve_order():
     
     while q.is_not_empty :
        print ("now serving ",q.deque_())
        time.sleep(2)
    

    




if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    order= OrdersQueue
    t1 =threading.Thread(target=(place_orders),args=(orders,))
    t2 = threading.Thread(target=(serve_order))

    t1.start()
    t2.start()
    # order.thread(order.serve_order)
        