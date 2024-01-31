strs = ["eat","tea","tan","ate","nat","bat"]
table = {}


for i in strs:
    key = "".join(sorted(i))
    if key in table:
        table[key] = table[key]+","+i
    else:
        table[key] = i

print(table)



