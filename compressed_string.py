str_value = "aabcccccaaa"
compressed_str = []

counter = 0

for i in range(len(str_value)):
    counter +=1
    if i + 1 >= len(str_value) or str_value[i] != str_value[i + 1]:
        compressed_str.append(str_value[i])
        compressed_str.append(counter)
        counter = 0

if len(compressed_str) >  len(str_value):
    print(compressed_str)



