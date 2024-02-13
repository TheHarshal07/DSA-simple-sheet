#Here we need to find Reverse of the s
def Reverse_s(s):
    # here we need to set two pointer that will point to first and last element
    a = 0
    b = len(s)-1
    # stop when a will be less than b
    while a<b:
        #Here we just need to swap the element 
        s[a],s[b] = s[b],s[a]
        a =+ 1
        b -= 1
    return s


st =["H","B","S"]
print(Reverse_s(st))



def Reverse(s, length):
    if length < 1:
        return ""
    if length == 1:
        return s[0]
    return s[length-1] + Reverse(s,length-1)

s = "Harshal"
n = len(s)
print(Reverse(s,n))