# Here we have three types of problems

# Type 1:
# we have givem row and column and we have to find out the element present at that position

def NCR(n,r):
    ans = 1
    for i in range(r):
        ans = ans*(n-i)
        ans = ans//(i+1)

    return ans


# Type 2: In which we have to print the nth row in in pascal's triangle

def generateRow(row):
    ans = 1
    ansRow = []
    ansRow.append(ans)
    for i in range(1,row):
        ans = ans*(row-i)
        ans = ans // i
        ansRow.append(ans)
    return " ".join(map(str,ansRow))



# Type 3: Important Type where we need to print the pascal's triangle

def pascalsTriangle(n):
    answer = []
    for i in range(1,n+1):
        answer.append(generateRow(i))
        
    return answer


row= 5
col = 3
print(NCR(row-1, col-1))
print(generateRow(row))
print(pascalsTriangle(row), end="")