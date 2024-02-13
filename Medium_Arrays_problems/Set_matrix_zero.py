# HEre we have to set matrix to zero 

#Brute Force
def markRow(arr,n,m,i):
    for j in range(m):
        if arr[i][j] != 0:
            arr[i][j] = -1

def markCol(arr,n,m,j):
    for i in range(n):
        if arr[i][j] != 0:
            arr[i][j] = -1

def setZero(arr,n,m):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                markRow(arr,n,m,i)
                markCol(arr,n,m,j)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                arr[i][j] = 0
    return matrix



#Better Approach
def setMat(arr,n,m):
    col = [0]*m
    row = [0]*n

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                col[j] = 1
                row[i] = 1

    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                arr[i][j] = 0

    return arr


matrix = [[1,1,1],[1,0,1],[1,0,1]]
n = len(matrix)
m = len(matrix[0])
print(setMat(matrix,n,m))