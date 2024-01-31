class Node:
    def __init__ (self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

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
    
    def delete_middle_node(self):
        index = self.get_length()//2
        counter = 0
        itr = self.head
        while itr.next:
            itr = itr.next
            if counter == index -1:
                itr.next = itr.next.next
            counter += 1
            

