'''
*
**
***
****
*****
****
***
**
*
This is the pattern
'''

def startpattern(n):
    for i in range(1,2*n-1+1):
        stars = i
        if (i>n):
            stars = 2*n-i
        for j in range(1,stars+1):
            print("*",end="")
        print("\r")
n = 5
startpattern(n)