# Here we gonna learn hwo to reverse the array

def Reverse(arr,n):
    result = ""
    for i in range(n,-1,-1):
        result += arr[i]
    return result


arr = [1,2,3,4,5]
n = len(arr)
print(Reverse(arr,n))