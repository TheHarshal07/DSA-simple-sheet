# Here we need to find kth smallest element in the array
# for e.g
# arr = [2,4,7,9,3] ==> One mothode is to sort the arrays and just return arr[k-1] element
                  # ==> same if you want to find the kth largest element just return arr[len(arr)-k]
import heapq



def findSmallestElement(arr1, k):
    if k <= 0:
        return []
    
    min_heap = []

    for num in arr1:
        if len(min_heap) < k:
            heapq.heappush(min_heap,-num)
        elif -num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, -num)

    result = [-x for x in min_heap]

    return sorted(result, reverse=True)

arr1 = [2,9,4,3,7]
k1 = 3
result = findSmallestElement(arr1,k1)
print(result)
    