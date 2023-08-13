f = int(input("Enter the number :"))
a,b,c=-1,1,0
s = []
for i in range(f+1):
    c= a+b
    a = b
    b = c
    if(i+1 == f+1):
        s.append(c)
    print(c,end=" ")
print(s)