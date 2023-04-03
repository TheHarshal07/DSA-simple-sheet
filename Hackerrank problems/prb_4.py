import math

def sit(N):
    return math.factorial(N-1) * math.factorial(2)

N = 4
print(sit(N))