a = [2,4,5,6,7]

b = 0
j = len(a) - 1

while b<j:
    a[b],a[j] = a[j],a[b]
    b += 1
    j -= 1

print(a)