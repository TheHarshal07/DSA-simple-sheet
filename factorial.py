'''
Here we are writing down the program for factorial number:
for example:
4! = 4*3*2*1 = 24

'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
n = 4
print(factorial(n))


