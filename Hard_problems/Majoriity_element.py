# Here we gonnaa find out the majority element in the array
# Time comeplexity - O(n^2)
# Space Complexity - O(n)
from collections import Counter 
def Majority(arr,n):
    lst = []
    for i in range(n):
        if(len(lst)==0 or lst[0]!= arr[i]):
            count = 0
            for j in range(1,n):
                if arr[j] == arr[i]:
                    count += 1
        if (len(lst)==2):
            break
    if count > n//3:
        lst.append(arr[i])
    return lst


#Better Approach
# Time complexity - O(n^2)
# Space complexity - O()
def HashmapMajority(arr,n):
    hashmap = {}
    stack = []
    for ele in arr:
        if ele in hashmap:
            hashmap[ele] += 1
        else:
            hashmap[ele] = 1
    for key, values in hashmap.items():
        if values > n//3:
            stack.append(key)
    return stack


# Better Approach
# T.C - O(n)
# S.C - O(n) as worst case
def Mapping(arr,n):
    counter = Counter(arr) 
    for num, count in counter.items():
        if count > (n//3):
            return num
    return -1



def Majprity(arr,n):
    lst = []
    for i in range(n):
        if (len(lst)==0 or lst[0]):
            count = 0
            for  j in range(1,n):
                if arr[j] == arr[i]:
                    count += 1
        if (len(lst)==2):
            break
        if count > (n//3):
            lst.append(arr[i])
    return lst

arr = [1,1,1,2,2,2,2,2,4,4,3,1,1]
print(Majprity(arr,len(arr)))
