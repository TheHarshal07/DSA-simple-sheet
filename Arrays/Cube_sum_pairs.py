import math
def cum_sum_pairs(num):
    n = len(num)
    count = 0
    for i in range(1,n+1):
        for j in range(0,i):
            if i**3 + j**3 == num:
                count += 1
    return count

num = 27
print(cum_sum_pairs(num))

