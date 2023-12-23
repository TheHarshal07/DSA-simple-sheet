'''
pattern:

E
D E
C D E
B C D E
A B C D E

'''

def pattern_17(n):
    for i in range(n):
        for j in range(i,-1,-1 ):
            print(chr(ord("E")-j), end=" ")
        print("\r")

n = 5
pattern_17(n)