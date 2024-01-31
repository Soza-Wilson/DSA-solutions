from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self,data):
        self.stack.append(data)
        self.push_min(data)
    

    def getMin(self):
        return self.min_stack[-1]
    
    def pop(self):
        data = self.stack.pop()
        self.pop_min(data)
        return data

    def push_min(self,data):
        if len(self.min_stack)==0:
            self.min_stack.append(data)
        if self.min_stack[-1]> data:
            self.min_stack.append(data)
    
    def pop_min(self,data):
        if data == self.min_stack[-1]:
            self.min_stack.pop()

    def add_values(self,data_list):
        for i in data_list:
            self.push(i)