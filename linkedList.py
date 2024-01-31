class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    

class linkedList:
    def __init__(self):
        self.head=None

    def add_data_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print_data(self):
        if self.head is None:
            print("head is empty")
            return
        iterator = self.head
        list_string = ''
        while iterator.next:
            list_string += str(iterator.data)+ '->'
            iterator=iterator.next
        
        print(list_string)

    def insert_end(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return
        iterate = self.head
        while iterate.next:
            iterate = iterate.next
        iterate.next = Node(data,None)
    
    def insert_values(self,data):
        for i in data:
            self.insert_end(i)
    def get_length(self):
        count = 0
        iterate =self.head
        while iterate:
            count += 1
            iterate = iterate.next
        return count
    
   
