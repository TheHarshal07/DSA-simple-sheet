'''
You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number


Input 1:
aA1_67

Input 2:
a987 abC012

Output 1:
1
Output 2:
0

'''

def CheckPassword(s,n):
    if n < 4:
        return 0
    elif s[0].isdigit():
        return 0
    
    cap = 0
    num = 0
    for i in range(n):
        if s[i]==" " or s[i]=="/":
            return 0
        elif s[i] >= 'A' and s[i] <= 'Z':
            cap += 1
        elif s[i].isdigit():
            num += 1
    if cap>0 and num >0:
        return 1
    else:
        return 0

strInput = input("Enter the password: ")
length = len(strInput)
print(CheckPassword(strInput, length))
