from collections import deque

class Node:
    def __init__ (self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node 
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self,data):
        for i in data:
            self.insert_at_end(i)
    def print_data (self):
        if self.head is None:
            print("linkedList is empty")
            return
        itr = self.head
        output = ''
        while itr.next:
            itr = itr.next
            output += str(itr.data) + '->'    
        return output
    
    def get_length(self):
        counter = 0
        itr = self.head
        while itr.next:
            itr= itr.next
            counter +=1
        return counter
    
    def reverse_list(self):
        stack = deque()
        output = []
        if self.head is None:
            print("can not reverse empty list")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
            if itr.data < itr.next.data or itr.next.next !=None:
                print(itr.data , " is greater than", itr.next.data)
            
        return self.print_data()
            