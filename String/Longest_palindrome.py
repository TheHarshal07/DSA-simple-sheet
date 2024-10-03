
def longestPalin(s):
    res = ""
    rlen = 0

    for i in range(len(s)):
        
        # Here we gonna find palindrome for even string by  initializing left and right pointer
        l, r = i,i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > rlen:
                res = s[l:r+1]     # ---> Concatination
                rlen = r - l + 1
            l -= 1
            r += 1
        # Now same logic will be applied for odd length
        l,r = i,i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > rlen:
                res = s[l:r+1]
                rlen = r - l + 1
            l -= 1
            r += 1
    return res

s = "aaaabbaa"
print("Longest palindrome is :",longestPalin(s))