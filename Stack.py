from collections import deque
class Stack:
    
    def __init__(self):
        self.stack = deque()

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
       return self.stack[-1]
    
    def info(self):
        return(dir(self.stack))
    
    def size(self):
         return len(self.stack)
    

   
             
                      


