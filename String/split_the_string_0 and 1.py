def maxSubStr(str):
        count_0 = 0
        count_1= 0
        
        fcount = 0
        
        for i in range(len(str)):
            if str[i] == "0":
                count_0 += 1
            else:
                count_1 += 1
            if count_0 == count_1:
                fcount += 1
                
        if count_0 != count_1:  # which is not possible
            return -1
        return fcount

string = "001100011101"
print(maxSubStr(string))