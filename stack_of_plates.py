from collections import deque

'''
First we will create a normal stack


'''

class Stack:
    def __init__(self):
        self.stack = deque()
        self.MAX = 10
        self.sub_list =[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]
      

class SetOfStacks:
    def __init__(self):
        self.MAX = 10
        self.sub_list =[]
        self.stack = Stack()
    
    def sub_stack(self,data):
            
        if len(self.sub_list)==0 or self.sub_list[-1].size() == 10:
            self.stack.push(data)
            self.sub_list.append(self.stack)
        elif self.sub_list[-1].size() < 10:
             self.sub_list[-1].push(data)
                    
    def add_value(self,data_list):
        for i in data_list:
            self.sub_stack(i)
     
    def pop(self):
        if self.sub_list[-1] == None:
            print('stack is empty')
            return
        return self.sub_list[-1].pop()
    
    def push(self,data):
        self.sub_stack(data)    
    
    def popAt(self,index):
        return self.sub_list[index].pop()



        # def __repr__(self) -> str:
        # pass


