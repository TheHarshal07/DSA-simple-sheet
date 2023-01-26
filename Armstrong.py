user = int(input("Enter the number :"))
result = 0
p = user
while user>0:
    rem = user%10
    result = result+(rem*rem*rem)
    user //= 10

if p==result:
    print("It is an armstrong number ",p)
else:
    print("It is not an armstrong number ",p)