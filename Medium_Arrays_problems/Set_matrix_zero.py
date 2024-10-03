# HEre we have to set colatrix to zero 

# Time complexity - O(N*M)*O(N*M)
#Space comlexity - O(1)

#Brute Force
def markRow(arr,row,col,i):
    for j in range(col):
        if arr[i][j] != 0:
            arr[i][j] = -1

def markCol(arr,row,col,j):
    for i in range(row):
        if arr[i][j] != 0:
            arr[i][j] = -1

def setZero(arr,row,col):
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                markRow(arr,row,col,i)
                markCol(arr,row,col,j)
    for i in range(row):
        for j in range(col):
            if arr[i][j] == -1:
                arr[i][j] = 0
    return matrix


# Time complexity - O(N*M)
# Space compleity - O(N) + O(M)]

#Hint - col array and row array will keep track of zeros in matrix

#Better Approach
def setcolat(arr,row,col):
    col1 = [0]*col
    row1 = [0]*row

    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                col1[j] = 1
                row1[i] = 1

    for i in range(row):
        for j in range(col):
            if row1[i] or col1[j]:
                arr[i][j] = 0

    return arr


matrix = [[1,1,1],[1,0,1],[1,0,1]]
row = len(matrix) # row
col = len(matrix[0]) # col 
print(setZero(matrix,row,col))