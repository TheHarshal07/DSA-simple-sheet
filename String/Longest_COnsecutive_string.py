# Here we have to find longest consecutive string given below
# String = aabbaa
# Output = aba
# we can solve this problem using stack
def longestconsecutive(ch):
    stack = []
    for s in ch:
        if len(stack) == 0:
            stack.append(s)
        else:
            if stack[-1] != s:  # Here we will have a,b
                stack.append(s)
    return "".join(map(str,stack))

ch = "aabbaa"
print(longestconsecutive(ch))