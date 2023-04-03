from collections import Counter

def count_arr(arr):
    count = Counter(arr)
    for key, values in count.items():
        print(f"{key} occure {values} time")

arr = [1,2,3,3,4,1,5,8,5]
count_arr(arr)