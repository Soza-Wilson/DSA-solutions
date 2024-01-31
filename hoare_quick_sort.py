

def swap_values(first_value,second_value,array):
    tmp = array[first_value]
    array[first_value] = array[second_value]
    array[second_value] = tmp


def partion(array,start,end):

#step 1 : in the fisrt step we will find the pivot index and find the start and end pointers in the array
    
    pivot_index = start
    start = pivot_index + 1
    
    while start < end :
# step 2 : we will move the start pointer until we find an element that is greater than pivot inde value 
        while start < len(array) and array[start] <= array[pivot_index]:
            start+=1
#step 3 :we will move end until value at ed is les than value at pivot index 
        while array[end] > array[pivot_index]:
            end -=1
#step 4 : then we will swap data at end and data at start by calling the swap function  
        if start < end:
            swap_values(start,end,array)   
    swap_values(pivot_index,end,array)
    return end

def quick_sort(array,start,end):

    if start < end : 
        pi = partion(array,start,end)
        quick_sort(array,start,pi-1) # left partion 
        quick_sort(array,pi+1,end) #right partion
    


if __name__ == "__main__":
    elements = [34,6,1,78,97,56,3,4,10]
    quick_sort(elements,0,len(elements)-1)

    # test cases 

    tests = [

         [34,6,1,78,97,56,3,4,10],
          [67,8,5,6,5,4,2,1,0],
          [0,1,3,5,7,9,56,78],
          []

    ]

    for elements in tests:
        quick_sort(elements,0,len(elements)-1)
        print("sorted arrays ", elements)




