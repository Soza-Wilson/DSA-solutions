'''
This class we are using a singly linked list to impliment the iterator design pattern 

'''


class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next



class LinkedList:
    def __init__(self) -> None:
        self.head = None 
        self.current = None

    def insert_at_begging(self,data):
        node = Node(data,self.head)
        self.head = node 

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next= Node(data,None)

    def insert_data_values(self,array):
        # funtion takes ana array and iterate through its valiables and inserts the valiables into the linked list 
        for i in array:
            self.insert_at_end(i)

    def print(self):
        if self.head is None:
            print ('list is empty')
            return
        iterator = self.head
        printData = ""

        while iterator.next:
            iterator = iterator.next
            printData += str(iterator.data) + '->'
        print(printData)

    
            
    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current:
            val = self.current.data
            self.current= self.current.next
            return val
        else:
            raise StopIteration







if __name__ == '__main__':
    list = LinkedList()
    list.insert_data_values([2,2,1,4,2,1,4,5,6,73,2])
   
    for i in list:
        print(i)
