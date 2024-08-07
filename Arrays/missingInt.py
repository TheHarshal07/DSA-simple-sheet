# Here we need to find the missing element in the given array
# We can find the missing element uding hashmap and sum formula

# We used sum formula to find the missing values in array 
# sum = (n(n+1)/2)\


#Brute Force - linear search
# Time complexity  - O(n^2)
def BruteApproch(arr,n):
    for i in range(1,n+1):
        flag = 0
        for j in range(0,n-1):
            if arr[j] == i:
                flag = 1
                break

        if flag == 0:
            return i

#Better Approach
#Time Complexity - O(2n)
# Space Complexity - O(n)
        
def betterApproch(arr,n):
    hash= {}
    for k in range(1, n+2):   # hash = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
        hash[k] = 0

    for i in range(n-1):      # hash = {1:1, 2:1, 3:1, 4:1, 5:0, 6:1, 7:1}
        hash[arr[i]] = 1

    for j in range(1,n+1):    # it will check and return ==> 5
        if hash[i] == 0:
            return i
        
def best_Arroach(arr,n):
    stack = []
    for i in range(1,n+1):
        if i not in arr:
            stack.append(i)
    return stack
        
# Optimal Approcch - Sum methode
# Time complexity - O(n)
def OptimalSum(arr,n):
    sum = int(n*(n+1)/2)
    res = 0
    for i in range(n-1):
        res += arr[i]
    
    return (sum-res)

# Optimal Approach - XOR methode
# Time complexity - O(n)
# But this would be slider faster thatn sum methode

def XorAppraoch(arrn,n):
    xor1 = 0
    xor2 = 0
    for i in range(n-1):
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ (i+1)
    xor2 = xor2 ^ n
    return xor1 ^ xor2

arr = [1, 2, 4, 6, 3, 7, 8]
n = 7
print(betterApproch(arr,n))
