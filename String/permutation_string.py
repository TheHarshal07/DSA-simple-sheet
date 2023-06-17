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

a = "ABC"
print("All permutation are : ")
ans = permute(a,answer)