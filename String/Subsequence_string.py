# Here we gonna print all subsequnece of the string 

# Time complexity - O(n^2)
# We can it out by recursion as well 
s = "abcd"
for i in range(len(s)):
    for j in range(i,len(s)+1):
        print(s[i:j],end=" ")
    print(" ")
    