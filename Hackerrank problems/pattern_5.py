rows = 5
k = 4 * rows - 6
for i in range(0, rows):
    for j in range(0,k):
        print(end=" ")
    k = k-2
    for i in range(0, 2*i-1):
        print("* ", end="")
    print("")

k = rows - 1
for i in range(rows, -1 , -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 2
    for j in range(0, 2*i-1):
        print("* ", end="")
    print("")
