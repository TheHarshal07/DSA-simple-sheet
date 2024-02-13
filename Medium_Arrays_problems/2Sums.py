# THe problem is to find the elements which sums get equivalent to the target
# Variety 1 - To check  whether the sum of the elements is equivalent to the target or not
# Variety 2 - To return the indext of that elements 



#Better Approach and optimal approach for Variety 2
# Time and space complexity is O(n)
def twosums(arr,n, target):
    hashmap = {}
    for i in range(n):
        num = arr[i]
        more = target - num
        if more in hashmap:
            return {num,more}  # return {{hashmap[more],i}}  --> to return index of the elements
        hashmap[num] = i
    return "No"

#Better approach for variety 1 
# Time and space complexity is - O(n)
def optimal(arr,n,target):
    left = 0
    right = n-1
    while(left <= right):
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return {left,right}
        if curr_sum < target:
            left += 1
        if curr_sum > target:
            right -= 1
    return "No"

arr = [2,3,6,8,11]
n = len(arr)
target = 14
print(optimal(arr,n,target))
