from collections import deque

str = "Let's take LeetCode contest"
map = {}
data_array = str.split(' ')
output = []

for i in range(len(data_array)):
    for j in data_array[i]:
        if i in map:
            map[i] = j + map[i]
        else:
            map[i] = j

for i in map:
    output.append(map[i])
string = ",".join(output)
print(string)



