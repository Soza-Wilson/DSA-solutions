def bubble_sort (array):
    size = len(array)

    for j in range(size-1):
        swapped = False
        for i in range(size -1- j):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i +1 ]
                array[i + 1] = tmp 
                swapped =True

        if not swapped:
            break



if __name__ == '__main__':
    array = [9,8,34,52,5,23,67]

    bubble_sort(array)
    print(array)