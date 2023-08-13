# Here we'll gonna find majority of an element whose count is greater than N/2
# So if N = 6 then there count should be greater thatn N/2 i.e. > 3

a= [2,3,1,2,2]
# Output would be 2, bcz 2 count is > N/2
# Brute force 
# Time complexity = O(n^2)
# Space complexity - O(1)

N = len(a)
count = 0
for i in range(N):
    for j in range(N):
        if a[i]==a[j]:
            count += 1
if (count>N/2):
    print(a[i])
    


# Better appraoch 
# Time complexity - O(n)
# Space Complexty - O(n)
hashmap = {}
N = len(a)
for i in range(len(a)):
    hashmap[a[i]] = i
for key in hashmap.values():
    if key > (N//2):
        print(a[i])



# Optimal Approach
# Time complexity - O()
count = 0
for i in range(len(a)):
    if count == 0:
        count = 1
        ele = a[i]
    elif (a[i]==ele):
        count += 1
    else:
        count =- 1
count1 = 0
for i in range(len(a)):
    if a[i]==ele:
        count1 += 1
    if (count1>(N//2)):
        print(ele)