'''
A = [2,4,6,8]
Output = A = [4*6*8, 2*6*8, 2*4*8, 2*4*6]
'''

def MultiplyArr(arr):
    
    n = len(arr)
    stack = []

    for i in range(n):
        res = 1
        for j in range(n):
            if i == j:
                pass
            else:
                res *= arr[j]
        stack.append(res)
    return stack


arr = [2,4,6,8]

print(MultiplyArr(arr))