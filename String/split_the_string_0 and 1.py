def maxSubStr(self,str):
        count1 = 0
        count2 = 0
        
        fcount = 0
        
        for i in range(len(str)):
            if str[i] == "0":
                count1 += 1
            else:
                count2 += 1
            if count1 == count2:
                fcount += 1
                
        if count1 != count2:  # which is not possible
            return -1
        return fcount