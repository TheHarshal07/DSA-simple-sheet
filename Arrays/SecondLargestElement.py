# Here we have to find out the second largest element in the array
 # ====> Brute force

a = [3,6,2,6,8,8]
n = len(a)-1
a.sort()
# Array looks like [2,3,6,6,8,8] and thing is for sure, last element would largest element
# in the array (n-1)

largest = n-1

for i in range(n-2):
    if (a[i]!=largest):
        second = a[i]
print(second)





# Better solution
# Time Complexity is O(2n)
largest = a[0]
for i in range(n):
    if a[i]>largest:
        largest = a[i]
slargest = -1
for i in range(n):
    if (a[i]>slargest and a[i]!=largest):
        slargest = a[i]

print(slargest)


# Optimal solution
# Time complexity is O(n)
largest = a[0]
slargest = -1

for i in range(1,n):
    if a[i]>largest:
        slargest = largest
        largest = a[i]
    elif(a[i]<largest and a[i]>slargest):
        slargest = a[i]
print(slargest)

