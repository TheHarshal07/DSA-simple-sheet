# Here we need to find the missing element in the given array
# We can find the missing element uding hashmap and sum formula

# We used sum formula to find the missing values in array 
# sum = (n(n+1)/2)

arr = [1,2,3,4,5,7,8,9,10,11]
n = 11

sum = int(n*(n+1)/2)
res = 0
for i in range(len(arr)):
    res += arr[i]

ans = sum - res

print(f"Missing element is {ans}")
