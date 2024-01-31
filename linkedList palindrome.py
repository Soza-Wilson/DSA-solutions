from collections import deque

class Node:
    def __init__ (self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        if data is None:
            print("data empty")
        else:
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
        itr = self.head
        newList = LinkedList()

        while itr.next:
            itr = itr.next
            stack.append(itr.data)
        while len(stack) >0:
            newList.insert_at_end(stack.pop())
        return newList.print_data()
    
    def check_palindrom(self):
        stack = deque()
        itr = self.head
        reversed_list = LinkedList()

        while itr.next:
            itr.next
            stack.append(itr.data)

        while len(stack) > 0:
            reversed_list.insert_at_end(stack.pop())
        