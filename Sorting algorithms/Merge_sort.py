# Merge sort
# '''
# It involve divide and merge
# Time complexity -> O(nlogn) - worst, best, average case
# space complexity -> O(n)

# '''

# def merge(arr,low,mid,high):
#     left = low
#     right = mid+1
#     temp = []
#     while(left<=mid and right <= high):
#         if (arr[left]<= arr[right]):
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1
    
#     while(left<= mid):
#         temp.append(arr[left])
#         left += 1
    
#     while(right<high):
#         temp.append(arr[right])
#         right += 1

#     for i in range(low, high+1):
#         arr[i] = temp[i-low]

# def merge_sort(arr,low,high):
#     if low >= high:
#         return
#     mid = int((low + high)/2)
#     merge_sort(arr,low,mid)
#     merge_sort(arr,mid+1,high)
#     merge(arr,low,mid,high)


def merging(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []

    while(left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while(left <= mid):
        temp.append(arr[left])
        left += 1
    
    while(right <= high):
        temp.append(arr[right])
        right += 1
    
    for i in range(low , high+1):
        arr[i] = temp[i-low]
    return arr



def merge(arr,low, high):
    if low >= high:
        return
    mid = int((low + high)/2)
    merge(arr,low, mid)
    merge(arr,mid+1, high)
    merging(arr,low,mid,high)


def mergingg(arr,low,mid,high):
    left = low 
    right = mid+1
    temp = []

    while(left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while(left <= mid):
        temp.append(arr[left])
        left += 1
    while(right <= mid):
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]
    return arr


def merggg(arr,low,high):
    if low>= high:
        return
    mid = (int(low + high)/2)
    merggg(arr,low,mid)
    merggg(arr,mid+1,high)
    mergingg(arr,low,mid,high)
arr = [8,7,6,5,4,3]
low = 0
high = len(arr)-1
merggg(arr,low,high)
print(arr)
