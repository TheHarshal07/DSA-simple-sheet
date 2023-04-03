def count_element(arr):
    count = 1
    max_val = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max_val:
            count += 1
            max_val = arr[i]
    return count




arr=[7,4,8,2,9]
print(count_element(arr))