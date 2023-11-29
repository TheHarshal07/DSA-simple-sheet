'''
1      1
12    21
123  321 
12344321

'''

def pattern_14(n):
    space = 2*(n-1)
    for i in range(1, n+1):
        
        for j in range(1, i+1):
            print(j, end="")
        #space
        for h in range(space):
            print(" ",end="")
        
        for k in range(i, 0, -1):
            print(k, end="")
        space -= 2
        print("\r")

n = 4
pattern_14(n)