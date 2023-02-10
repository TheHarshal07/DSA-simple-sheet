# Here we need to find kth smallest element in the array
# for e.g
# arr = [2,4,7,9,3] ==> One mothode is to sort the arrays and just return arr[k-1] element
                  # ==> same if you want to find the kth largest element just return arr[len(arr)-k]
import heapq
arr = [1,2,2,9,3,4,5]
k = 5
#First we'll sort the array

# print(arr.sort())  # ==> you can directly used sort function
# print(arr[k-1])

# l =0 
# h = len(arr)-1
# while l<=h:  
#     arr[l],arr[h] = arr[h],arr[l]
#     l += 1
0
#     h -= 1
# print(arr)

print(heapq.nsmallest(k,arr)[k-1])
print(heapq.nlargest(k,arr)[k-1])  #==> in max heap always top element will be max
