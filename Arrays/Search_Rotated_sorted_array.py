#Here we need to search in rotated sorted array for given element
#Basically we have given target index and we have to find out that element of target index

def sorted(arr):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr.index(arr[i])
    else:
        return -1

arr = [12,3,5,2,8]
target = 5
# output would be = 2