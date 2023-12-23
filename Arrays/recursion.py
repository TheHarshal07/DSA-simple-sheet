
def Recursion(n):
    if n == 5:
        return
    print(n)
    n += 1
    Recursion(n)

n = 0
Recursion(n)

'''
Sum of N natural numbers using recursion ( parametrized way )
  
'''

def recursion(i, sum):
    if i < 1:
        return sum
    return recursion(i-1, sum+i)

n = 3
print(recursion(n,0))


''' Here is the recursive function for n natural number '''

def f(n):
    if n == 0:
        return 0
    return n + f(n-1)

n = 5
print(f(n))