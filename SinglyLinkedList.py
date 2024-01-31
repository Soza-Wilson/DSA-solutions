class Node:
    def __init__(self,data =None, next=None):
        self.data = data
        self.next = next
     

class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node 

    def print_data(self):
        if self.head is None:
            print("linked list is empty")
            return
        datalist = ''
        itr = self.head
        while itr:
            datalist += str(itr.data) + '>'
            itr= itr.next
        print(datalist)
    def get_length(self):
        counter = 0
        itr = self.head
        if self.head is None:
            print("linked llist is empty")
            return
        else:
            while itr.next:
                counter +=1
                itr = itr.next
        return counter
            
                    
    
    def add_data_list (self,data):
        for i in data:
            self.insert_at_end(i)
        
            
    def insert_at_end (self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr= itr.next
        itr.next = Node(data,None)

    def insert_middle(self,data):
        length = self.get_length()
        if length<0:
            raise Exception("linked in length < 0")
        if self.head is None:
            self.insert_at_beginning(data)
            return
        counter  = 0 
        itr= self.head
        index = self.get_length()//2
        while itr.next:
            if counter is index-1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            counter += 1
        
    def insert_at (self,data,index):
        if index <0 or index >= self.get_length:
            raise Exception(" index out of range ")
        if self.head is None:
            self.insert_at_beginning(data)
            return
        counter = 0
        itr = self.head
        while itr.next:
            if counter is index -1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            counter +=1
    


    def delete_at(self,index):
        if index < 0 or index >self.get_length():
            raise Exception("index out of range")
        if index ==0:
            self.head = self.head.next
            return 
        counter = 0
        itr = self.head
        while itr.next:
            if counter is index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            counter +=1


    def insert_by_value(self,insert_after,value):
        if self.head is None:
            print("linkedlist is empty")
            return
        itr = self.head
        while itr.next:
            if itr.data == insert_after:
                print("we here ")
                itr.next = Node(value,itr.next)
                return
            itr = itr.next


    def delete_by_value(self,value):
        if self.head is None:
            print("LinkedList is empty")
            return
       
        counter = 0
        itr = self.head
        while itr.next:
            if itr.next.data==value:
                counter
                itr.next= itr.next.next          
            counter +=1
            itr= itr.next
        
    def get_sum (self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        data = 0
        while itr.next:
            data += itr.data
            itr =itr.next
        return data
                   
    # def get_conc(self):
    #     if self.head is None:
    #         print("list is empty")
    #         return
    #     itr = self.head
    #     output = ''
    #     while itr.next:
    #         itr =itr.next
    #         output = str(itr.data) + output
    #     return output

