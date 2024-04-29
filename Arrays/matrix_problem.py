# Here we have to solve the problem in the matrix


arr = [[1,2,3,4],[4,5,6,7],[7,8,9,10,],[11,12,13,14]]

row = len(arr)
for i in range(row):
    col = len(arr[i])
    for j in range(col):
        print(arr[i][j], end="")
    print()

print("Output of this program is : ")
for i in range(row):
    if (i % 2 == 0):
        for j in range(col):
            print(arr[i][j], end=" ")
    else:
        for j in range(col-1, -1,-1):
            print(arr[i][j], end=" ")