#Here we need to find Reverse of the s
def Reverse_s(s):
    s = s[::-1]
    string = s.split(" ")
    # here we need to set two pointer that will point to first and last element
    a = 0
    b = len(string)-1
    # stop when a will be less than b
    while a<b:
        #Here we just need to swap the element 
        string[a],string[b] = string[b],string[a]
        a =+ 1
        b -= 1
    return " ".join(string)

st ="Hello world"
print(Reverse_s(st))



def Reverse(s, length):
    if length < 1:
        return ""
    if length == 1:
        return s[0]
    return s[length-1] + Reverse(s,length-1)


def Reverse(string,n):
    if n < 1:
        return ""
    if n == 1:
        return string[0]
    return string[n-1] + Reverse(string,n-1)
    
def reverseWord(s,n):
    ss = Reverse(s,n)
    return ss

s = "Harshal"
n = len(s)
print(reverseWord(s,n))