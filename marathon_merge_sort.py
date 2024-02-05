from collections import deque




def merge_sort(array,sorting_value,decending):


    if len(array) <= 1:
        return 
    mid_point = len(array)//2 
    left = array[:mid_point]
    right  = array[mid_point:]

    merge_sort(left,sorting_value,decending)
    merge_sort(right,sorting_value,decending)

    merge(left,right,array,sorting_value,decending)

def merge(a,b,array,sorting_value,decending):
    
    i = j = k = 0
    len_a =len(a)
    len_b =len(b)
    while i < len_a and j < len_b:
        if a[i][sorting_value] <= b[j][sorting_value]:
           
                
            array[k]=a[i]
            i+=1

        else:
            array[k]=b[j]
            j+=1
        k+=1

    while i < len_a:
        array[k]=a[i]
        i+=1
        k+=1
    while j < len_b:
        array[k] = b[j]
        j+=1
        k+=1
    
        










if __name__ =="__main__":
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    

   
    merge_sort(elements,"time_hours")
    print(elements)