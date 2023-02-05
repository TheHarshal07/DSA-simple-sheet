#Move negative numbers to begining and positive to end with constant extra space
a = [-12,11,-13,-5,6,-7,5,-3,-6]

# a.sort()
# # print(a)
# for i in a:
#     print(i,end=" ")

j=0
for i in range(len(a)):
    if (a[i]<0):
        a[i],a[j] = a[j],a[i]
        j = j + 1
print(a)

n =[]
p = []
for i in range(len(a)):
    if (a[i]>0):
        n.append(a[i])
    else:
        p.append(a[i])
a[:] = n+p
print(a[:])
