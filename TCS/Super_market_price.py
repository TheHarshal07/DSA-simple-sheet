'''
The task here is to design the program such that given the code of any item N the product (multiplication) of all the digits of value should be computed(price).

Input :

5244 -> Value of N

Output :
160 -> Price 

Explanation:
From the input above 
Product of the digits 5,2,4,4

5*2*4*4= 160

Hence, output is 160.

'''
def Market_price(num):
    n = len(str(num))
    result = 1
    for i in range(n):
        rem = num % 10           # 5244 --> 4 will be stored in rem ( % give you reminder)
        result = result * rem    # result * rem = 1 * 4 = 4 ( result will update and become 4)
        num //= 10               # This will give you 524 from 5244

    return result

num = 5244
print(Market_price(num))
