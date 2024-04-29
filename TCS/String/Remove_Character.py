# Here we have to remove the character from the string

def Remove_Char(String, Str2):
    stack = []
    for i in String:
        if i in Str2:
            continue
        else:
            stack.append(i)
    return ''.join(stack)

Str1 = "Harry"
Str2 = "Ha"
print(Remove_Char(Str1,Str2))
            