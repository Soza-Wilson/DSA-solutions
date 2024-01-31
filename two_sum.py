nums = [2,7,11,15]
target = 9

map = {}

for i,n in enumerate(nums):
    diff = target - n
    if diff in map:
        print(map[diff] , i)
    else:
        map[n] = i


