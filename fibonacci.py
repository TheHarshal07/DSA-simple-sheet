f = int(input("Enter the number :"))
a,b,c=-1,1,0

for i in range(f):
    c= a+b
    a = b
    b = c
    print(c,end=" ")