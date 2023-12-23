# Here we have to check the given string is palindrome or not

def CheckPalindrome(str):
    l = len(str)
    if str[:l] == str[::-1]:
        return True
    else:
        return False

string = "haah"
print(CheckPalindrome(string))


def MathChalllege(num):
    total = 0
    s = 'sss'
    for i in range(1, num+1):
        total += i
    
    return str(total)+s

n = 4
print(MathChalllege(n))


