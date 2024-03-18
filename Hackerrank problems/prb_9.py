def OddPattern(n):
    for i in range(n):
        for j in range(i+1):
            if j % 2 == 0:
                print("1",end="")
            else:
                print("0",end="")
        print("\r")

n = 5
OddPattern(n)


print("------Start Patterns -----------------")

def startPattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print("\r")


def ReverseStartPattern(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print("*",end="")
        print("\r")

n = 5
startPattern(n)
ReverseStartPattern(n)