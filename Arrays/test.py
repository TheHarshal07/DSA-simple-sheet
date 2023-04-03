
def arr(a):
    n = len(a)
    if (n==0):
        return 0
    elif (n==2):
        if a[0]>=a[1]:
            return 0
        else:
            return 1
    else:
        if (a[0]>=a[1]):
            return 0
        elif (a[n-1]>=a[n-2]):
            return n-1
    for i in range(n):
        if (a[i]>=a[i+1] and a[i]>=a[i-1]):
            return i
        
a1 = [11,23,34,16]
print(arr(a1))
        
        

