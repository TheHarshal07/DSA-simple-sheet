# '''
#     *
#    ***
#   *****
#  *******
# *********

# '''
# number = 5
# def StarPattern(n):
#     for i in range(n):
#         #space
#         for j in range(n-i-1):
#             print(" ", end="")
#         #stars
#         for k in range(2*i+1):
#             print("*", end="")
#         #space
#         for l in range(n-i-1):
#             print(" ", end="")
#         print("\r")


# StarPattern(number)


# def ReverseStartPattern(N):
#     for i in range(N):
#         #space
#         for j in range(i):
#             print(" ",end="")
#         #Stars
#         for k in range(2*N-(2*i+1)):
#             print("*",end="")
#         #space
#         for l in range(i):
#             print(" ",end="")
#         print("\r")

# ReverseStartPattern(number)







def pattern(num):
    for i in range(num):
        #space
        for j in range(num-i-1):
            print(" ", end="")
        #start
        for k in range(2*i+1):
            print("*",end="")
        #space
        for l in range(num-i-1):
            print(" ",end="")
        
        print("\r")
number = 5
pattern(number)


def reversePattern(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*n-(2*i+1)):
            print("*", end="")
        for k in range(i):
            print(" ", end="")
        print("\r")

num = 5 
reversePattern(num)


