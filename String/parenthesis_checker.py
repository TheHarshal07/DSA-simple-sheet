def ispar(x):
        stack = []
        dict = {")":"(","}":"{","]":"["}
        
        for i in x:
            if i in dict.values():
                stack.append(i)  # appended ==> (, {, [
            elif stack and dict[i] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return stack == []

s="{[()]}"
print(ispar(s))