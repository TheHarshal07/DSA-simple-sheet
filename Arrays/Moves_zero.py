# Moves all zeroes to end of the array

def movesZeros(arr):
    j = -1
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            j = i 
            break
    
    for k in range(j+1,n):
        if arr[k] != 0:
            arr[k],arr[j] = arr[j],arr[k]
            j += 1
    return arr


arr = [0,4,6,0,4,0]
print(movesZeros(arr))