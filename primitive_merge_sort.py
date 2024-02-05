def merge_sort(array):
    if len(array) <= 1 :
        return array
    mid_point = len(array) //2 

    left =array[:mid_point]
    right = array[mid_point:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted_lists(left,right)

def merge_sorted_lists(a,b):
    len_a = len(a)
    len_b = len(b)
    sorted_list = []
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j] :
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
         sorted_list.append(a[i])
         i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    
    return sorted_list


if __name__ == "__main__" :
    b = [45,73,2,4,1,4,54,12,87]
    print(merge_sort(b))

  