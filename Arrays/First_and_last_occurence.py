# Here we have to find first and last occurence in given Array
# We have to return index of the first and last occurence
#Time complexity = O(n^2)
# Sapce complexity = O(1)

def occurence(arr,x):
    f = -1
    l = -1
    for i in range(len(arr)):
        if arr[i] == x:
            f = i
            break
    for j in range(f,len(arr)):
        if arr[j] == x:
            l = j
    return f,l

ar = [1,2,3,4,4,4,4,6]
a =4 
print(occurence(ar,a))


# Time compelexity = O(nlogn)
# Space complecity = O(1)

def occurence(arr,x):
    start = 0
    end = len(arr)-1

    while (start <= end and (arr[start]!= x or arr[end]!= x)):
           
           if arr[start]!=x:
               start += 1
           if arr[end]!= x:
               end -= 1
    if (start > end):
        return -1 ,-1
    return start, end

h = [1,2,3,4,5,5,5,6]
n = 5
print(occurence(h,n))
        
               
