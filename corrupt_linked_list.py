'''
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the 
beginning of the loop. 
DEFINITION 
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so 
as to make a loop in the linked list. 

'''



class Node:
    def __init__(self,data,next):
        self.data = data 
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        

    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    '''
    Printing does not work after inserting the last node ( 
    inserting the last node create a loop As the last node points at the head 
        )
    '''
    def print(self):
        if self.head is None:
            print ('linked list is empty')
            return
        return_list = ''
        itr = self.head
        while itr.next:
            return_list += str(itr.data) +'->'
            itr = itr.next
        return return_list
            
    def insert_values(self,data_list):
        for i in data_list:
            self.insert_at_beginning(i)

    '''
    to detect the loop in the linkedlist we will create hashset , while iterating through the list we will add the data to the the hashset 
    -- we will return the data of  the node pointing to the node that already exists in the hash_set 
    
    '''

    def detect_loop(self):
        if self.head is None:
            print ('linked list is empty')
            return
        itr = self.head
        hash_set = set()
        while itr.next:
            itr= itr.next
            if itr.next.data in hash_set:
                print (itr.next.data)
                break
            hash_set.add(itr.data)
            

        
    '''
    Inserting at the end creates a loop As the last not points at the head 
    '''    

    def insert_at_end(self,data):
        if self.head==None:
            self.head = Node(data,None)
        itr = self.head
        while itr.next:
            itr = itr.next
            if itr.next is None:
                itr.next = Node(data,self.head)
                break


           
            
    '''
    
    
    '''

