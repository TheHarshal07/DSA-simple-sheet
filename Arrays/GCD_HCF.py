'''
GCD - Greatest common divisor or ( HCF = Highest common factor)

for e.g: n1 = 15,  n2 = 20
thi GCD(20, 15) = 5

'''
# Time complexity - O(min(n1,n2)
def GCD(n1, n2):
    gcd = 1
    for i in range(1, min(n1,n2)):
        if ((n1 % i == 0) and (n2 % i == 0)):
            gcd = i
    return gcd


def lcm(n1,n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    
    while(True):
        if ((greater % n1 == 0) and (greater % n2 == 0)):
            lcm = greater
            break
        greater += 1
    
    return lcm
        
n1 = 4
n2 = 6
print(GCD(n1, n2))



'''
Methode - Eucledian methode

GCD(n1, n2) = GCD(n1-n2, n2) - It takes bit more time for execution

Note - When one of them (n1 or n2) become zero, The other one is GCD

optimise way is :
GCD(n1,n2) = GCD(n1 % n2, n2)

'''

# Time complexity - O(log(min(1,b)))
def gcd(a, b):
    while (a > 0 and b > 0):
        if a>b:
            a = a % b
        else:
            b = b % a
    
    if a == 0:
        return b
    else:
        return a

a = 20
b = 15
# print(gcd(a,b))