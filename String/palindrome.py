# Here we have to check the given string is palindrome or not

def CheckPalindrome(str):
    l = len(str)
    if str[:l] == str[::-1]:
        return True
    else:
        return False

string = "haah"
print(CheckPalindrome(string))


#optimal approch
def is_palindrome(s,start,end):
    if start >= end:
        return 1
    if s[start] != s[end]:
        return 0
    return is_palindrome(s,start+1, end-1)

arr = "abcba"
start = 0
end = len(arr)-1
print(is_palindrome(arr,start,end))

def MathChalllege(num):
    total = 0
    s = 'sss'
    for i in range(1, num+1):
        total += i
    
    return str(total)+s

n = 4
print(MathChalllege(n))


