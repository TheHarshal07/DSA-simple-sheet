# Find out the leaders in array

def learders(arr):
    n = len(arr)
    li = []
    maxi = arr[n-1]
    li.append(maxi)

    for i in range(n-2, -1,-1):
        if arr[i] > maxi:
            li.append(arr[i])
            maxi = arr[i]
    return list(reversed(li))

arr = [ 4,2,5,6,1,2]
a = learders(arr)
print(a)