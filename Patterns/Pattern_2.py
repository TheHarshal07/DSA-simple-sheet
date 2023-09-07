'''
This pattern we have to print

*
**
***
****

'''

def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print("\r")


def ReversePattern(n):
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print("*",end="")
        print("\r")


# Optimise solution
def pattern(n): # TC - O(n) and SC - O(n)
    li = []
    for i in range(1,n+1):
        li.append("*"*i)
    print("\n".join(li))



number = int(input("Enter the number :"))
pattern2(number)
print("\n")
ReversePattern(number)
print("\n")
print("Optimise Version: ")
pattern(number)

