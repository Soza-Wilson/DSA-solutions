



def find_dup(array):
    
    '''
    we are tring to find duplicate using the floys tortoise and hare algrothm
    -step 1 : we assign both slow and fast pointer at the head 
    -step 2 : we iterate both pointer slow moves in each node while fast moves by two
    -step 3 : if the two node meet we know that we have  a duplicate 
    -step 4 : we move the slow node to the head and make the fast node move by 1 
    -step 5 : then we return the new meeting point 
    '''


    # this example we will using 
    slow = 0
    fast = 0 

    while True:
        slow= array[slow]
        fast = array[array[fast]]

        if slow == fast:
            break
    slow = 0
    while slow != fast :
        slow = array[slow]
        fast = array[fast]
    print(slow)


  


   
                
            

               

        


if __name__=='__main__':

    find_dup([1,2,3,4,2,4,2])




    