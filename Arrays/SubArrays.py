# Here we need to find the subarrays from the given array

a = [1,-2,5,-3,6,-8,6]
# # a = [6,-3,-10,0,2]

sum = 0
max = a[0]
hashmap = {}
for i in range(len(a)):
    sum += a[i]
    if sum>max:
        max = sum 
        hashmap[a[i]] = 1
    elif sum<0:
        sum=0
    
for key in hashmap.keys():
    print(key,end=" ")




# def longestConsecutive(nums):
#     longest = 0

#     for x in nums:
#         currNum = x
#         currStreak = 1
#         while (currNum+1)     in nums:
#       -+
# -+
# - +      currNum += 1
#             currStreak += 1
#         longest = max(currStreak, longest)
#     return longest

# n = 5
# nums = [3, 4, 6, 7, 8]

# ans = longestConsecutive(nums)
# print("Length of longest consecutive subsequence in nums =", ans)

#Here we will find the subarrays from given array

import sys
h = [1,-2,-1,4,6]
max = -sys.maxsize-1
sum=0
start = 0
end = 0
for i in range(len(h)):
    sum += h[i]

    if sum > max:
        max = sum
        end = i
    
    if sum <0:
        sum =0
        start = i+1

print(h[start:end+1])
    