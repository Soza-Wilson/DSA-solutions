
def swap(first_value,second_value,array):
    temp = array[first_value]
    array[first_value] = array[second_value]
    array[second_value] = temp



def partion(array):

    p_index = 0
    i_index = 0
    pivot= len(array)-1
    while array[p_index] < array[pivot]:
        p_index += 1
        i_index = p_index
    while array[i_index] > array[pivot]:
        i_index +=1

    swap(p_index,i_index,array)



def quick_sort(array):
    partion(array)

if __name__ == "__main__":
    array = [11, 9, 7, 29, 2, 15, 28]
    quick_sort(array)
    print(array)

    


