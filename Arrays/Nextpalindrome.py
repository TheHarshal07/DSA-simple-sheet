# To generate a program that finds the next largest palindrome number after a given input,

def palindrome(n):
    num = str(n)
    if num == num [::-1]:
        return num
    
def Nextpalindrome(n):
    if palindrome(n):
        return n
    else:
        while not palindrome(n):
            n = n + 1
    return n
    
num = 24
print(Nextpalindrome(num))