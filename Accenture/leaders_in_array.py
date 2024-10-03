# To find out the leaders in array

def leaders(arr):
    n = len(arr)
    li = []
    maxi = arr[n-1]
    li.append(maxi)

    for i in range(n-2, -1,-1):
        if arr[i]>maxi:
            li.append(arr[i])
            maxi = arr[i]
    return list(reversed(li))

arr = [16,17,4,3,5,2]
print(leaders(arr))




