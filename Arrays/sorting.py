# here we will going to sort the array

def sorting(ar):
    n = len(ar)-1
    j = 0
    while j<n:
        if ar[j] > ar[j+1]:
            ar[j],ar[j+1] = ar[j+1], ar[j]
            j = -1
        j += 1
    
    return ar


arr = [4,6,2,1,9]
a = sorting(arr)
print(a)