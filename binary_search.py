def binary_search(array,value):
    left_index = 0
    mid_point = 0
    right_index = (len(array)-1)
    

    while left_index <= right_index:
        mid_point = (left_index + right_index) //2 
        mid_value = array[mid_point]

        if mid_value == value:
            return mid_point
        if mid_value < value:
            left_index = mid_point + 1

        else:
            right_index = mid_point -1
    
    return -1
   



if __name__ == '__main__':
    array_values = [1,2,3,4,5,6,7,8,9,10,11]
    search_value = 10

    index = binary_search(array_values,search_value)
    print('value is at', index)