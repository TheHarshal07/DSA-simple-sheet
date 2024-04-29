'''
Here we are gonna genearting a fibonaaci series
i.e --> 0 1 1 2 3 5 --( -1+1 = 0, 0+1 = 1, 1+1 = 2, 2+1 = 3 and so on)

'''
num = 5
a,b,c=-1,1,0

for i in range(num):
    c= a+b
    a = b
    b = c
    print(c,end=" ")




