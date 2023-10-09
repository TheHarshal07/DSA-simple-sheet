def pattern(n):
    for i in range(1,n):
        if i==1:
            print(i)
        print(n)
        n = n*10

num = 10
pattern(num)