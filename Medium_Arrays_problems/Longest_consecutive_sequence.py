# Here we have to fing out the longeset consecutive sequence inside the array
# For e.g - arr = [ 1,5,2,3,4,100,200] Herer --> Consecutive is 1,2,3,4,5
import sys
# This is Brute Force
def linear_search(arr1,num):
    for i in range(len(arr1)):
        if arr1[i] == num:
            return True
        else:
            return False

def longest_consecutive(arr,n):
    longest = 1
    count = 0
    for i in range(n):
        x = arr[i]
        count = 1
        while(linear_search(arr,x+1)):
            x += 1
            count += 1

        longest = max(longest,count)
    return longest


# Better Appraoch
# Step 1 - Sort the array
# Step 2 - Check by the prious item

def Longe_consecutive(arr):
    arr.sort()
    lastSmaller = -sys.maxsize-1 
    count = 0
    longest = 1
    n = len(arr)
    for i in range(n):
        if arr[i]-1 == lastSmaller:
            count+= 1
            lastSmaller = arr[i]
        elif (lastSmaller != arr[i]):
            count = 1
            lastSmaller = arr[i]
        longest = max(longest, count)
    return longest




# Optimal Approach
# Time Complexity - O(N) + O(N*2) ~ O(3*N)
# Sapce complexity - O(N)

#Step 1 - store all elements in Set data structure
#Step 2 - Iterate through set data structure
def longConsec(arr):
    s = set()
    n = len(arr)
    count = 0
    longest = 1

    for i in range(n):
        s.add(arr[i])
    for ele in s:
        if ele-1 not in s:
            count = 1
            x = ele
            while x+1 in s:
                x += 1
                count += 1
        longest = max(longest,count)
    return longest

arr = [1,6,10,2,4,3,5,11,13,12]
print(longConsec(arr))



arr = [1,6,10,2,4,3,5,11,13,12]
# print(Longe_consecutive(arr))



arr = [1,6,10,2,4,3,5,11,13,12]
# print(longest_consecutive(arr,len(arr)))



