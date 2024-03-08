# Here we need to find the peak element in the array which is not samller than adjacent element 
# [12,3,14] ==> In this case peak element is 14
def ar(arr):
    n = len(arr)
    if(n==1):
        return 0
    elif (n==2):
        if(arr[0]>=arr[1]):
            return 0
        else:
            return 1
    else:
        if (arr[0]>=arr[1]):
            return 0
        else:
            if (arr[n-1]>=arr[n-2]):
                return n-1
    for i in range(n):
        if (arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
            return i

a = [1,3,4]
print(ar(a))


# To solve the same problem using binary search...
#Here the time complexity is O(logn)


def abc(arr):
    n=len(arr)
    low = 0
    high = n-1
    
    while(low<=high):
        mid = int((low+high)/2)

        if (mid==0 or arr[mid]>=arr[mid+1]) and (mid==n-1 or arr[mid]>=arr[mid-1]):

            return mid
        
        elif(arr[mid]<=arr[mid+1]):
            low = mid+1
        else:
            high = mid-1

    return -1


arr2= [1, 8, 1, 5, 3]
print(abc(arr2))
