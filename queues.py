from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def deque(self,data):
        self.buffer.appendleft(data)

    def enque(self):
       return self.buffer.pop()
    
    def is_empty(self):
        if len(self.buffer)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.buffer)

    