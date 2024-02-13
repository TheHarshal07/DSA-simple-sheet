#Here we have to rotate the matrix to 90 degree.
def RotateMatrix(matrix,n,m):
    
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            rotated[j][n-i-1] = matrix[i][j]
    return rotated



def LeftRotatedArr(matrix,n,m):
    rotate = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            rotate[i][j] = matrix[n-j-1][i]

    return rotate


#Better Approach
def RoataeArr(matrix,n,m):
    for i in range(n):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
    
    return matrix

    


matrix = [[1,2,1],[1,0,1],[1,1,1]]
n = len(matrix)
m = len(matrix[0])
print(LeftRotatedArr(matrix,n,m))