'''
Here we have to find the element which is equilibrium

'''

def find_equilibrium(arr):
    sumi = 0
    rightSum = 0
    n = len(arr)
    for i in range(n):
        sumi += arr[i]
    for i in range(n):
        sumi -= arr[i]

        if (sumi == rightSum):
            return i+1
        
        rightSum += arr[i]

    return -1

arr = [1,2,3,3]
print(find_equilibrium(arr))