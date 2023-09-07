# Here we will remove the element from the sorted array
# So basically our output would be, just remove duplicates and print it

# Brute force
# Time Complexity = O(n)
# Space Complexity = O(n)
d = [1,1,2,2,5,5]
s= set()
for i in range(len(d)):
    s.add(d[i])
print(s)








# Optimal Solution
# Time Complexity = O(n)
# Space Complexity = O(1)

a = [1,1,2,2,3,3,3,4]
i = 0
for j in range(1,len(a)-1):
    if a[j] != a[i]:
        a[i+1] = a[j]
        j += 1
print(j + 1)
