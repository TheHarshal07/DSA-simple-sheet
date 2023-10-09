'''
1
01
101
0101
10101

This is pattern

'''
def flip_pattern(n):
    for i in range(n):
        if (i%2==0):
            start = 1
        else:
            start = 0
        for j in range(0,i+1):
            print(start, end="")
            start = 1- start
        print("\r")

number = 5
flip_pattern(number)