# insertion sort
'''
It always takes an element and place in it correct position
Time complexity: O(n2) - worst case
                 O(n)  -  best case
'''
def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    return arr



def INsert(arr,n):
    for i in range(n):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j], arr[j-1] = arr[j-1],arr[j]
            j -= 1
    return arr

arr = [8,7,6,5,4,3,2,1]
n= len(arr)
print(INsert(arr,n))