'''
Here we have to return non repeating element in the array

'''

def Non_repeating(arr):
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num,0) + 1
    for num in arr:
        if hashmap[num] == 1:
            return num
    return 0

arr = [-1, 2, -1, 3, 2]
print(Non_repeating(arr))

