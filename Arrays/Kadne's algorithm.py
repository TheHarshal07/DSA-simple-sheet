import sys
def subarray(arr):
    max = -sys.maxsize-1 # Smallest possible value of the variable
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

        if sum > max:
            max = sum
       
        if sum < 0:
            sum = 0
    return max

ar = [1,-2,4,-1,2,3]
print(subarray(ar))


# This is code to return entire subarray from the given list

def subarray(arr):
    max = -sys.maxsize-1 # Smallest possible value of the variable
    sum = 0
    start_index = 0
    end_index = 0
    for i in range(len(arr)):
        sum += arr[i]

        if sum > max:
            max = sum
            end_index = i
        if sum < 0:
            sum = 0
            start_index = i + 1
    max_subarray = arr[start_index:end_index + 1]       
    return max_subarray

ar = [1,-2,4,-1,2,3]
print(subarray(ar))