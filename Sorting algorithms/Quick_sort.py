# Quick sort
'''
It sort the array in the ascending order

algorithm 

step 1: Pick up the pivot from the array
step 2: place in it correct place in sorted array
step 3: smaller on the left side and larger on the right side

'''

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while(i<j):
        while(arr[i] <= pivot and i <= high-1):
            i += 1
        while(arr[j] > pivot and j >= low+1):
            j -= 1
        
        if (i<j): arr[i], arr[j] = arr[j],arr[i]
        
    arr[low],arr[j] = arr[j],arr[low]
    return j

def Quick_sort(arr,low,high):
    if low < high:
        Pindex = partition(arr,low,high)
        Quick_sort(arr,low,Pindex-1)
        Quick_sort(arr,Pindex+1,high)
    return arr

arr = [8,7,6,5,4,3,2]
low = 0
high = len(arr)-1
Quick_sort(arr,low,high)
print(arr)


