# Code for palindrome

h = int(input("Enter the number :"))
p =h
result=0
while h>0:
    rem = h%10
    result = (result*10) + rem
    h //= 10

if p == result:
    print("It is palindrome number ",p)
else:
    print("It is not palidrome number ",p)


s = ["H","A","R","S","H","A","L"]
print("".join(s))
print(s)
print(*s)