
def practise(n):
    num = 1
    for i in range(n):
        for k in range(n-i):
            print(" ",end="")
        for j in range(i):
            print(num, end=' ')
            num = num + 1
        print("\r")



practise(5)