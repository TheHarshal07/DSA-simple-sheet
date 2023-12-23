'''
**********
****  ****
***    ***
**      **
*        *
**      **
***    ***
****  ****
**********

Hint - Divide the pattern horizontally

'''

def pattern_18(n):
    space = 0
    for i in range(n):
        #stars
        for j in range(n-i):
            print("*", end="")
        #space
        for k in range(space):
            print(" ",end="")
        #stars
        for l in range(n-i):
            print("*", end="")
        space += 2
        print("\r")

n = 5
pattern_18(n)


def pattern(a):
    space = 2*a-2
    for i in range(a):
        #stars
        for j in range(i+1):
            print("*", end="")
        #space
        for k in range(space):
            print(" ", end="")
        for l in range(i+1):
            print("*",end="")
        space -= 2
        print("\r")
n = 5
pattern(n)