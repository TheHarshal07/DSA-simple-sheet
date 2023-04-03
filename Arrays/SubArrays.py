# Here we need to find the subarrays from the given array

a = [1,-2,5,-3,6,-8,6]

sum = 0
max = a[0]
hashmap = {}
for i in range(len(a)):
    sum += a[i]
    if sum>max:
        max = sum
        hashmap[a[i]] = 1
    elif sum<0:
        sum=0
    
for key in hashmap.keys():
    print(key,end=" ")

