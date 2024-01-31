
def bubble_sort(elements,sorting_value):

   

   
    size = len(elements)
    for j in range(size-1):
        swapped = False
        for i in range(size - 1):
            if elements[i][sorting_value] > elements[i+ 1][sorting_value]:
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = tmp
                swapped = True
        if not swapped:
            break

    print(elements)       


if __name__ == "__main__":

    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements,"device")






