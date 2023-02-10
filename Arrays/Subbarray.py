#Sub array with given sum
#for e.g a = [1,2,4,5,7]
# N = 5, s = 12

class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       if s==0:
           return [-1]
       i=0
       j=0
       sm=0
       while j<len(arr):
            sm+=arr[j]
            if sm<s:
               j+=1
            elif sm==s:
                return [i+1,j+1]
            elif sm>s:
                while sm>s:
                    sm-=arr[i]
                    i+=1
                if sm==s:
                    return [i+1,j+1]
                j+=1
       return [-1]    
      
a = [1,2,3,7,5]
s=12
ob = Solution()
print(ob.subArraySum(a,len(a),s))