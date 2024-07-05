def ispar(x):
        stack = []
        dict = {")":"(","}":"{","]":"["}
        for i in x:
            
            if i in dict.values():
                stack.append(i)  # appended ==> (, {, [
            elif stack and dict[i] == stack[-1]: #Here "stack" --> it is not empty AND Checking wether the opening symbol at the top                            
                                                 #  of the stack is matched with opening symbol in dict
                stack.pop()
            else:
                return False
        
        
        return stack == []

s="{[()]}"
print(ispar(s))