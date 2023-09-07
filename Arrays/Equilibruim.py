#Here we have to find out the equilibruim point from the array
def equilibruim(arr):
    if(len(arr) == 1):
        return 1
    sum = 0
    rightSum = 0
    for i in range(len(arr)):
        sum += arr[i]  # Here we have to find sum of the all the element in the array
    for i in range(len(arr)):
        sum -= arr[i]   # Here substracting the element from the sum 
        if (sum == rightSum): # Checked is the left sum  is equal to the rightsum or not 
            return i+1
        rightSum += arr[i]
    return -1


arr = [1,3,5,2,2]
print("Position of the that element is :",equilibruim(arr))
