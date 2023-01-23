#To reverse the array in python
def rev(a):
    i = 0
    j = len(a)-1
    while i<j:
        t = a[i]
        a[i] = a[j]
        a[j] = t
        i+=1
        j-=1

n = int(input("Enter n "))
l = []
for i in range(n):
    l.append(int(input()))
rev(l)
print(l)