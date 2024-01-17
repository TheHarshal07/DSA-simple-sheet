# Here we gonna find duplicates in array

# 1 - Brute force
# Time complexity = O(n^2)
t = [2,3,4,2,1,1]

for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i] == t[j]:
            # print(t[i])
            pass
            

            

# 2 - Bettter solution
# We can make use of Hashmap
# Space complexity = O(n)  bcz we're using hashmap yo store the elements
e = [2,3,4,2,1,1]
hashmap = {}
s = set()
for i in e:
    if i in hashmap:
        hashmap[i] += 1
        s.add(i)
    else:
        hashmap[i] = 1
        hashmap.items

# return ''.join(map(str,s)) --> to return the element without square brackets
        


# 3 - Optimal Solution
# Time complexity = O(n)
# Sapce complexity = O(1)

def FindDuplicates(a):
    n = len(a)
    s = []
    for i in range(n):
        index = a[i]%n
        # print(index)
        a[index] += n
        print(a[index])

    for i in range(n):  
        if a[i]/n >= 2:
            s.append(i)
    return s

arr = [2,3,4,2,1,1]
h = FindDuplicates(arr)
print(h)


