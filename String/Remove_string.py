# Input:
# tiger     -> input string A
# ti        -> input string B
# Output:
# ger       -> Output string C


def RemoveString(s1,s2):
    ans=""
    for i in s1:
        if i in s2:
            continue
        else:
            ans += i
    
    return ans


s1 = "Hello"
s2 = "llo"
print(RemoveString(s1,s2))
