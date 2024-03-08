#Here we gonna find the missing number in the array

def missing(arr,n):
    sum = int(n*(n+1)/2)
    res = 0
    for i in range(n-1):
        res += arr[i]
    ans = sum - res
    return ans

arr = [1,2,3,5,6,7]
n = len(arr)
print(missing(arr,n))