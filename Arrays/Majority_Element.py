# Here we'll gonna find majority of an element whose count is greater than N/2
# So if N = 6 then there count should be greater thatn N/2 i.e. > 3

a= [2,3,1,2,2]
# Output would be 2, bcz 2 count is > N/2
N = len(a)
for i in range(N):
    count = 0
    for j in range(N):
        if a[i]==a[j]:
            count += 1

    if (count>N/2):
        print(a[i])
    