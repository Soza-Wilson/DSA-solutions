str = ["eat","tea","tan","ate","nat","bat"]

map = {}
output = []


for i in str:
    key = "".join(sorted(i))
    if key in map:
        map[key] += ","+i
    else:
        map[key] = i
for i in map:
    output.append(map[i]) 
output
    

