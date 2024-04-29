# Here we have to find the mean and median from the given array


def Mean(arr):
    n = len(arr)
    sumi = 0
    for i in range(n):
        sumi += arr[i]

    return float(sumi / n)

def Median(arr):
    n = len(arr)
    sorted(a)
    if n % 2 !=0:
        return float(arr[int(n/2)])
    return float((arr[int((n-1)/2)] + arr[int(n/2)])/2.0)

a = [1, 3, 4, 2, 7, 5, 8, 6]
print(Mean(a), Median(a))