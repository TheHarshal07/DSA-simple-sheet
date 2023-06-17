# class Solution(object):
#     def countAndSay(self, n):
#         """
#         for e.g
#         1
#         11
#         21
#         1211
#         111221 This is gonna be series with n = 5
#         """
#         if n == 1:
#             return "1"
#         seq = self.countAndSay(n-1)
#         res = ""
#         c = 1

#         for i in range(len(seq)):
#             if i == len(seq)-1 or seq[i] != seq[i+1]:
#                 res += str(c) + seq[i]
#                 c = 1
#             else:
#                 c += 1
#         return res
    




def longestPalindrome( s):
    """
    :type s: str
    :rtype: int
    """
    r = ""
    rlen = 0

    for i in range(len(s)):
        # Here we gonna find palindrome for odd string by  initializing left and right pointer
        l, r = i,i

        while l >= 0 and r <= len(s) and s[l] == s[r]:
            if (r-l+1) > rlen:
                r = s[l:r+1]     # ---> Concatination
                rlen = r - l + 1
            l -= 1
            r += 1
        # Now same logic will be applied for odd length
        l,r = i,i
        while l >= 0 and r <= len(s) and s[l] == s[r]:
            if (r-l+1) > rlen:
                r = s[l:r+1]
                rlen = r - l + 1
            l -= 1
            r += 1
    return r

s = "aaabbabb"
print(longestPalindrome(s))

