'''
The task here is to sort the items based on their levels of risk in the array

[1,0,2,0,1,0,2]-> Element of arr[0] to arr[N-1], while input each element is separated by new line.

Output :
0 0 0 1 1 2 2  -> Element after sorting based on risk severity 
'''
def arr_sort(num):
    arr = []
    for i in range(len(num)):
        arr.append(num[i])
    for j in sorted(arr):
        print(j, end="")
    
arr = [1,0,2,0,1,0,2]
arr_sort(arr)