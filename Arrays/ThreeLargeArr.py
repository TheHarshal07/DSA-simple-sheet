# To find three largest number in the arrays..
# Time complexity will be O(n) and space will be O(1)
import sys
l = [14965,2500,1228,3200,2800]

first = second = third = -sys.maxsize-1


for i in range(len(l)):
    if l[i]>first:
        third = second
        second = first
        first = l[i]

    elif l[i]>second:
        third = second
        second = l[i]

    elif l[i]>third:
        third = l[i]
print("Three largest numbers are ",first,second,third)

