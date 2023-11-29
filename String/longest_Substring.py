'''
Here we need to find out the longest Substring in given string
and return length of the longest substring

''' 

def longestSubstring(str):
    max_len = 0
    n = len(str)
    start = 0
    end = 0
    if n <= 1:
        return str
    
    # This for the odd length
    for i in range(n-1):
        l,r=i,i
        while(l>=0 and r < n):
            if str[l] == str[r]:
                l -= 1
                r += 1
            else:
                break 

        length = r-l-1
        if length > max_len:
            max_len = length
            start = l + 1
            end = r-1

    for i in range(n-1):
            l,r= i, i+1
            while(l>=0 and r<n):
                if str[l]== str[r]:
                    l -= 1
                    r += 1
                else:
                    break
    
            length = r-l-1
            if (length > max_len):
                max_len = length
                start = l+1
                end = r-1
        
    return str[start:end+1]

# s = "aaaabbaa"
# print(longestSubstring(s))





def substring(strr):
    n = len(strr)
    max_len = 0
    star = 0
    endd = 0

    if n <= 1:
        return strr
    for i in range(len(strr)):
        l,r =i,i
        while(l>=0 and r<n):
            if strr[l] == strr[r]:
                l -= 1
                r += 1
            else:
                break
        length = r-l-1
        if length > max_len:
            max_len = length
            star = l+1
            endd = r-1 
    return strr[star:endd+1]

g = "aaaabbaa"
print(substring(g))