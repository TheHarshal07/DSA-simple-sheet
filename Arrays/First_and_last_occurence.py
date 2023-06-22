# Here we have to find first and last occurence in given Array
# We have to return index of the first and last occurence
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

