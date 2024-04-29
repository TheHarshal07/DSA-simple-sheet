'''
Here we have to find out the array which is subset of another array

'''

def Array_Subset(arr1,arr2):
 
    for i in arr2:
        if i not in arr1 or arr2.count(i) > arr1.count(i):
            return "No"
    return "Yes" 

arr1 = [11, 7, 1, 13, 21, 3, 7, 3]
arr2 = [11, 3, 7, 1, 7]

print(Array_Subset(arr1,arr2))