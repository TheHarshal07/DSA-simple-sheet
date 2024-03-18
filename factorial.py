'''
Write down the program for factorial number:

'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = 4
print(factorial(n))


