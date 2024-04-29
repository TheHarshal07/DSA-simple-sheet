
def print_pattern(rows):
    num = 1
    for i in range(rows):
        for j in range(i):
            print(" ", end="")
        for k in range(rows - i):
            print(num, end="")
            num += 1
        print()

num = 4
print(print_pattern(num))