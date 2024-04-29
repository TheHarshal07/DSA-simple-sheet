'''
Here we gonna create possible paths from start index to the end index

'''
#Brute force
def Possible_paths(m,n):
    if(m==1 or n==1):
        return 1
    return Possible_paths(m-1,n) + Possible_paths(m,n-1)


#Better Approch
def Better_approch(m,n):
    mat = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]
    
    return mat[m-1][n-1]


#Optimal Approach
def Optimal_approch(m,n):
    dp = [1]*n
    for i in range(m-1):
        for j in range(1,n):
            dp[j] += dp[j-1]
            
    
    return dp[n-1]

m,n = 3,3
print(Better_approch(m,n))