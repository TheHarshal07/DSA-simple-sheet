def permute(s,answer):
    if (len(s) == 0):
        print(answer, end=" ")
        return
    for i in range(len(s)):
        ch = s[i]
        l = s[0:i]
        r = s[i+1:]
        res = l + r
        permute(res,answer+ch)
                   
answer = ""



def get_permute(string, i = 0):
    
    words = []
    if i == len(string):
        print("".join(string))
    
    for j in range(i, len(string)):
        
        words = [c for c in  string]
        
        words[i], words[j] = words[j],words[i]

        get_permute(words, i+1)


get_permute("abc")


a = "ABC"
print("All permutation are : ")
ans = permute(a,answer)

# a = "ABC"
# print(a[:0])


