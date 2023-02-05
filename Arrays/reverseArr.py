# this code is for reverse the array contain number
a = [2,4,5,6,7]

b = 0
j = len(a) - 1

while b<j:
    a[b],a[j] = a[j],a[b]
    b += 1
    j -= 1

print(a)


# Reverse the array contain string

a = "Harshal"
n = len(a)-1

result = ""
for i in range(n,-1,-1):
    result += a[i]
print(result)
