# Pattern for Numbers
'''
1
12
123
1234

'''
def NumberPattern(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        print("\r")


# Rverse the Number Pattern
def ReverseNumberPattern(n):
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print(j+1,end="")
        print("\r")


number = int(input("Enter the number : "))
NumberPattern(number)
print("\n")
ReverseNumberPattern(number)