# Here we have to print the matrix in spiral manner

def spiralMatrix(matrix,n,m):
    left = 0
    top = 0
    right = m - 1
    bottom = n -1
    stack = []
    for i in range(left, right+1):
        stack.append(matrix[top][i])
    top += 1

    # moving from top to bottom
    for i in range(top , bottom+1):
        stack.append(matrix[i][right])
    right -= 1

    # moving from right to left
    if(top <= bottom):
        for i in range(right, left-1,-1):
            stack.append(matrix[bottom][i])
        bottom -= 1

    #moving from bottom to top
    if left <= right:
        for i in range(bottom, top-1, -1):
            stack.append(matrix[i][left])
        left += 1

    return stack

matrix = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
n = len(matrix)
m = len(matrix[0])
print(spiralMatrix(matrix,n,m))