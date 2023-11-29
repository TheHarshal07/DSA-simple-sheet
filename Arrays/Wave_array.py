# Wave array problem :
'''
We have given sorted array, in we have to arrange them lime 
arr[1]>= arr[2]<= arr[3]>=arr[4]<=arr[6]........

for e.g:
n = 5
arr = [1,2,3,4,5]
output = 2,1,4,3,5
'''

def Wave_array(arr):
    n = len(arr)
    for i in range(0,n,2):
        if ((n-1)%2==0 and n-1 == i):
            break
        else:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [1,2,3,4]
print(Wave_array(arr))