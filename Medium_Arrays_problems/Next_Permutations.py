# Here we have to find out the next permutations 

def permutations(arr,n):
    # Find out the breaks points
    ind = -1
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            ind = i 
            break
    if ind == -1:
        arr.reverse()
        return arr
    
    # Find out the greates element but smallest one
    for i in range(n-1,ind,-1):
        if arr[i] > arr[ind]:
            arr[i],arr[ind] = arr[ind],arr[i]
            break

    #Reversing the half index
    arr[ind+1:] = reversed(arr[ind+1:])
    return arr

A = [3, 1, 2]
n = len(A)
print(permutations(A,n))