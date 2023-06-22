# Here we have to find value which is equal to index
def value_index(arr):
    s = []
    if len(arr) == 1:
        return 1
    for i in range(len(a)):
        if arr[i] == i+1:
            s.append(arr[i])
    return s



a = [12,2,3,5,9]
print(value_index(a))
