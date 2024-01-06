# Merge sort
'''
It involve divide and merge
Time complexity -> O(nlogn) - worst, best, average case
space complexity -> O(n)

'''

def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []
    while(left<=mid and right <= high):
        if (arr[left]<= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while(left<= mid):
        temp.append(arr[left])
        left += 1
    
    while(right<high):
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

def merge_sort(arr,low,high):
    if low >= high:
        return
    mid = int((low + high)/2)
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)

arr = [8,7,6,5,4,3]
low = 0
high = len(arr)-1
merge_sort(arr,low,high)
print(arr)
