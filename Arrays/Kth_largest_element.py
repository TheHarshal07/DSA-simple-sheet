# HEre we have to find out the kth largest element in the array
import  heapq

def smallestElement(arr,k):
    arr.sort()
    return arr[:k]

def largestElement(arr,k):
    arr.sort()
    arr.reverse()
    return arr[:k]

arr = [1,4,6,-1,8]
k = 3
print(largestElement(arr,k))
print(smallestElement(arr,k))



def findKLargestElements(arr, K):
    if K <= 0:
        return []

    min_heap = []
    
    for num in arr:
        if len(min_heap) < K:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    return sorted(min_heap, reverse=True)

arr1 = [1,2,3,4,5]
k = 3
numdd = findKLargestElements(arr1,k)
print(numdd)

