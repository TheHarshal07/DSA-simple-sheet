# Count the subbarray with given sum

def CountTheArray(arr,n,num):
    count = 0
    for i in range(n):
        for j in range(i,n):
            sumi = 0
            # subbArray_sum = sum(arr[i:j+1])
            for k in range(i,j+1):
                sumi += arr[k]

            if sumi == num:
                count += 1
    return count


def CountArray(arr,n,num):
    count = 0
    for i in range(n):
        sumi = 0
        for j in range(i,n):
            sumi += arr[j]

            if sumi == num:
                count += 1
    
    return count

arr = [1,2,3,-3,1,1,1,4,2,-3]
n = len(arr)
num = 3
print(CountArray(arr,n,num))