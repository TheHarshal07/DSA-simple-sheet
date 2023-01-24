a = [0,2,1,2,0]

# Here will used swapping
# Time complexity is O(n2)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)