user = int(input("Enter the number :"))
result = 0
p = user
len_input = len(str(user))
while user>0:
    rem = user%10
    result = result+(rem ** len_input)
    user = user//10

if p==result:
    print("It is an armstrong number ",p)
else:
    print("It is not an armstrong number ",p)