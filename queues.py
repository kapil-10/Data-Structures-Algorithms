from collections import deque
import time
import threading

class line():
    def __init__ (self):
        self.queue = deque()

    def add(self,value):
        return self.queue.appendleft(value)
    
    def remove(self):
        return self.queue.pop()
    
    def peek(self):
        return self.queue[-1]
    
    def is_empty(self):
        if len(self.queue) == 0:
            print('The queue is empty')

    def size(self):
        return len(self.queue)
    
#     Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python

# Pass following list as an argument to place order thread,

place = ['pizza','samosa','pasta','biryani','burger']
dd_queue = line()

def doordash_recived(orders):
    for order in orders:
        dd_queue.add(order)
        print ('The order recived is for ',order)
        time.sleep(0.5)

def doordash_delivered():
    time.sleep(1)
    
    while True:
        ns = dd_queue.remove()
        print('The oder which got delivered is ',ns)
        time.sleep(2)



if __name__ == '__main__':

    place = ['pizza','samosa','pasta','biryani','burger']


    t1 = threading.Thread(target = doordash_recived,args = (place,))
    t2 = threading.Thread(target = doordash_delivered)

    t1.start()
    t2.start()
    t1.join()
    t2.join()


