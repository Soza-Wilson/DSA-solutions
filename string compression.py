str= 'aabcccccaaa'
count = 0
output = []
for i in range(len(str)):
    count += 1
    if i + 1 >= len(str) or str[i] != str[i + 1]:
        
        output+= "" + str[i]
        output.append(count)
        count = 0


if len(output) > len(str):
    print(str)