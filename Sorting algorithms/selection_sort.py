# Selection sort
'''
Select the minimun and swap them 

'''
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini],arr[i] = arr[i],arr[mini]
    return arr

arr = [1,3,5,2,6,8]
print(selectionSort(arr))