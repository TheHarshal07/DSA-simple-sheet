'''
    *
   ***
  *****
 *******
*********

'''
number = 5
def StarPattern(n):
    for i in range(n):
        #space
        for j in range(n-i-1):
            print(" ", end="")
        #stars
        for k in range(2*i+1):
            print("*", end="")
        #space
        for l in range(n-i-1):
            print(" ", end="")
        print("\r")


StarPattern(number)


def ReverseStartPattern(N):
    for i in range(N):
        #space
        for j in range(i):
            print(" ",end="")
        #Stars
        for k in range(2*N-(2*i+1)):
            print("*",end="")
        #space
        for l in range(i):
            print(" ",end="")
        print("\r")

ReverseStartPattern(number)

