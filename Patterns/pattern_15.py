''''
A
AB
ABC
ABCD


'''

def Pattern_15(n):

    for i in range(n):
        for j in range(i+1):
            print(chr(ord("A")+j), end=" ")
        print("\r")
n = 5
Pattern_15(n)

print(" ")
print("--------------------------------------------")
print(" ")


'''
ABCDE
ABCD
ABC
AB
A

'''

def Revers(n):
    for i in range(n,-1,-1):
        for j in range(i):
            print(chr(ord("A")+j), end=" ")
        print("\r")

n = 5
Revers(n)


print(" ")
print("--------------------------------------------")
print(" ")

def pattern(n):
    for i in range(0, n):
        for j in range(i+1):
            print(chr(ord("A")+i), end=" ")
        print("\r")

n = 5
pattern(n)