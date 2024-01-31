str = "Let's take LeetCode contest"
array = str.split(" ")
output =[]
map = {}

for i in range(len(array)):
    for j in array[i]:
        if i in map:
            map[i] = j+map[i] 
        else:
            map[i] = j


for i in map:
    output.append(map[i])

" ".join(output)
