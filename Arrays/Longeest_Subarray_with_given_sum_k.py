# Here we have to find out the longest subbarray with given subbarray

# Brute force approch
# Time complexity = O(n^2)
def LongestSubbarray(arr,k):
    n = len(arr)
    lengh = 0
    for i in range(n):
        sumi = 0
        for j in range(i,n):
            sumi += arr[j]
            if sumi == k:
                lengh = max(lengh,j-i+1)
    return lengh


# Better Approach - Hashing







arr = [1,2,3,1,1,4,5]
n = len(arr)
k = 3
print(LongestSubbarray(arr,k))