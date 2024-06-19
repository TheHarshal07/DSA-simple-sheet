# Here we have to rearrange the element in the array without altering the order of the array

# Brute Force Approach
def rerrangeElement(arr,n):
    pos = []
    neg = []
    for i in range(n):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    for j in range(n//2):
        arr[2*j] = pos[j]
        arr[2*j+1] = neg[j]
    
    return arr





# Optimal approach
# Time and space complexity - O(n)
def rearrange(arr,n):
    n = len(arr)
    pos = 0
    neg = 1
    ans = [0]*n

    for i in range(n):
        if arr[i] < 0:
            ans[neg] = arr[i]
            neg += 2
        else:
            ans[pos] = arr[i]
            pos += 2
    return ans



# Veritey 2 problem
# What if i left some elements may be positive or may be negative I have to add that at the end of the array

def varietyProb(arr,n):
    pos = []
    neg = []
    n = len(arr)

    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index += 1

    return arr


arr = [1,2,-4,-5]
n = len(arr)
print(rerrangeElement(arr,n))