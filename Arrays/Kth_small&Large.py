# Here we need to find kth smallest element in the array
# for e.g
# arr = [2,4,7,9,3] ==> One mothode is to sort the arrays and just return arr[k-1] element
                  # ==> same if you want to find the kth largest element just return arr[len(arr)-k]
import heapq



def findSmallestElement(arr1, k):
    if k <= 0:
        return []
    
    max_heaq = []

    for num in arr1:
        if len(max_heaq) < k:
            heapq.heappush(max_heaq,-num)
        elif -num > max_heaq[0]:
            heapq.heappop(max_heaq)
            heapq.heappush(max_heaq, -num)

    result = [-x for x in max_heaq]

    return sorted(result, reverse=True)

arr1 = [1, 23, 12, 9, 30, 2, 50]
k1 = 3
result = findSmallestElement(arr1,k1)
print(result)
    