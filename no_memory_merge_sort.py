
def merge_sort(array):
    if len(array) <= 1:
        return 
    mid_point = len(array)//2 
    left = array[:mid_point]
    right  = array[mid_point:]

    merge_sort(left)
    merge_sort(right)

    merge(left,right,array)

def merge(a,b,array):
    
    i = j = k = 0
    len_a =len(a)
    len_b =len(b)
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
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
    




if __name__ == "__main__":
    elements = [2,6,5,11,0,2,1,3,4]
    merge_sort(elements)
    print(elements)
