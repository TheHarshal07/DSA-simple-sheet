def Pythagoral(a):
    if a % 2 == 0:
        n = 1
        m = a//2
    else:
        m = a//2 + 1
        n = m-1
        return [m**2-n**2, 2*m*n, m**2+n**2]
    
n = 5
print(Pythagoral(n))


# /If I want to find out the Pythogoral triplet for limit

def triplet(limit):
    c,m =0,2

    while c < limit:
        for n in range(1,m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if c > limit:
                break

            print(a,b,c)
        
        m = m + 1


limit = 20
triplet(limit)



