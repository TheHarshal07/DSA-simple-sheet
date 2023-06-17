#Here we have to find longest repeating subsequence 
df = {}
def long(s1,s2,n,m):
    if n == 0 or m == 0:
        return 0
    elif (n,m) in df:
        return df[(n,m)]
    else:
        if s1[n-1] == s2[m-1] and n!=m:
            c = 1 + long(s1,s2,n-1,m-1)
        else:
            c1 = long(s1,s2,n-1,m)
            c2 = long(s1,s2,n,m-1)
            c = max(c1,c2)
        df[(n,m)] = c
        return c
str = "axxxy"
print(long(str,str,len(str),len(str)))
    