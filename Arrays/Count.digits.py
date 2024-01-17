'''

Here we have to count the integer

n = 756
output = 3

'''

# def count_digit(n):
#     count = 0

#     while(n>0):
#         num = n % 10
#         count += 1
#         n //= 10
#     return count

# n = 756
# print(count_digit(n))




def twoSum(arr, target, n):
    # Write your code here.
    stack = []
    seen = set()
    for element in arr:
        comp = target - element
        if comp in seen:
            return True

        seen.add(element)
    return ' '.join(map(str, stack))

arr = [1,2,3,5,5,5]
target = 8
n = 6
print(twoSum(arr, target, n))
        
