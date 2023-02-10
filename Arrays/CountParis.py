# Here time complexity is O(n)
a = [1,5,1,7,1]
t = 6

s = set()
count = 0
for element in a:
    comp = t - element
    if comp in s:
        count += 1
    s.add(element)
print(count)



# Here time complexity is O(n2)
sum = 6
count = 0
for i in range(len(a)):
    for j in range(i+1):
        if (a[i]+a[j] == sum):
            count += 1
print(count)