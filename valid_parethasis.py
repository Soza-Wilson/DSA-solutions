from collections import deque


class Stack:


    def __init__(self):
        self.stack= deque()

    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

        
    def add_items(self,values):
        for i in values:
            self.push(i)
    
    def size(self):
        return len(self.stack)



   
       
      

    def is_match(self,ch1,ch2):
        self.map = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        return self.map[ch1] == ch2



    def check_parethasis(self,value):
        for i in value:
            if i == "(" or i == "{" or i == "[":
                self.push(i)
            if i == ")" or i == "}" or i == "]":
                if self.size==0:
                    return False
                if not self.is_match(i,self.pop()):
                    return False
                
            