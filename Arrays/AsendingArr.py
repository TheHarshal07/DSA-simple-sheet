# Input will be the a = [1,2,0,3,1]
#Here we need to use three pointer approch 
#Time complexity is O(n)
a = [0,1,2,0,1,2]

l = 0 
m = 0
h = len(a)-1

while m<=h:
    if (a[m] == 0):
        a[l],a[m] = a[m],a[l]
        l = l+1
        m = m+1
    elif (a[m] == 1):
        m = m + 1
    else:
        a[m],a[h] = a[h],a[m]
        h = h-1
print(a)



a1 = [0,2,1,2,0]

# Here will used swapping
# Time complexity is O(n2)
for i in range(len(a1)):
    for j in range(i+1,len(a1)):
        if a1[i] < a1[j]:
            a1[i],a1[j] = a1[j],a1[i]
print(a1)