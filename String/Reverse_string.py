#Here we need to find Reverse of the string
def Reverse_string(s):
    # here we need to set two pointer that will point to first and last element
    a = 0
    b = len(s)-1
    # stop when a will be less than b
    while a<b:
        #Here we just need to swap the element 
        s[a],s[b] = s[b],s[a]
        a =+ 1
        b -= 1
    return setattr


st =["H","B","S"]
print(Reverse_string(st))
