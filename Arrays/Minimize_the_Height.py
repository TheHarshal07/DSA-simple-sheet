# This is problem where we have to minimize the height of the tower
# SO basically we have given an array where each element in the array represent height of tower and we 
# have to minimize the maximum difference between the height
# But we have on constraint is k either we have to increment or decrement the height of tower by k
''' for example: [ 3, 9, 12, 16 ,20]  
for min ==> if I increase 3 by k and so dinfinetly I have to decrease the 9 by k so that I can get min difference
for max ==> if I decrease the 20 by k so definitely I have to increase the 16 by k so that I'll get min difference

'''
def TowerHeight(arr,n,k):
    arr.sort()
    ans = arr[n-1]-arr[0]

    smallest = arr[0]+k
    largest = arr[n-1]-k

    for i in range(1,n):
        if arr[i]-k <0:
            continue
        else:
            mi = min(smallest,arr[i]-k)
            mx = max(largest, arr[i-1]+k)

            ans = min(ans, mx-mi)
    return ans

a = [3, 9, 12, 16, 20]
n = len(a)
k = 3
print(TowerHeight(a,n,k))