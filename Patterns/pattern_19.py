'''
*        *
**      **
***    ***
****  ****     
**********
****  ****
***    ***
**      **
*        *


'''

def pattern_19(n):
    space = 2*n-2
    for i in range(1,2*n-1+1):
        stars = i
        if (i>n): stars = 2*n - i
        #stars
        for j in range(1,stars+1):
            print("*",end="")
        #space
        for k in range(space):
            print(" ", end="")
        #stars
        for l in range(1,stars+1):
            print("*", end="")
        print("\r")
        if i<n: space -= 2
        else: space += 2

n = 5
pattern_19(n)
