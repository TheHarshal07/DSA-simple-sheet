def sort_arr(arr):
    arr.sort(key=lambda x:x)
    return arr

arr = [1,0,1,2,0,2]
sort = sort_arr(arr)
print(sort)