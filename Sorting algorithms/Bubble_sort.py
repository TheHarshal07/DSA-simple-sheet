# Bubble sort
'''
Push the maximun to the last by adjencent swaps
Time complexity : O(n2) - worst case    
                  O(n) - Best case 

'''
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1,-1,-1):
        didswap = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                didswap = 1
                print("swapping")
        if (didswap == 0):   # This is for best case
            break
    return arr

arr = [8,7,6,5,4,3]
print(bubble_sort(arr))