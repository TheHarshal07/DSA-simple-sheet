'''
Here we have to rotate the array in cyclick manner ( left rotate )

'''

def reverse(arr, start, end):
    while(start <= end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr

def Optimal_reverse(arr,k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, n-k-1)
    reverse(arr, n-k, n-1)
    reverse(arr, 0, n-1)
    return arr


# Optimal Approach
# T.C - O(n)
def Sliccing(arr,k):
    n = len(arr)
    k = k % n
    arr[:] = arr[k:] + arr[:k]
    return arr


arr = [ 1,2,3,4,5]
k = 2
print(Sliccing(arr,k))