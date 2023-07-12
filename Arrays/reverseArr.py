# this code is for reverse the array contain number
a = [2,4,5,6,7]

b = 0
j = len(a) - 1

while b<j:
    a[b],a[j] = a[j],a[b]
    b += 1
    j -= 1

# print(a)



# Reverse the array contain string
a = "Harshal"

# Sapce complexity is O(n)
n = len(a)-1
result = ""
for i in range(n,-1,-1):
    result += a[i]
print(result)


# Sapce complexity is O(1)
a = list(a)
start = 0
end = len(a)-1
while start <= end:
    a[start],a[end] = a[end],a[start]
    start += 1
    end -= 1
a = "".join(a)
print(a)

