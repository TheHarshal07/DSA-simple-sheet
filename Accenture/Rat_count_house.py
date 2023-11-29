'''
The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument
 ‘r’ represents the number of rats present in an area,
‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number,
where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2

Output : 4

'''


def countRats(r, uni, n):
    arr = [2,8,3,5,7,4,1,2]
    totalFoodRequired = r * uni
    totalfood = 0
    house = 0

    for house in range(n):
        totalfood += arr[house]
        if totalfood >= totalFoodRequired:
            break
    if totalFoodRequired > totalfood:
        return 0 
    return house + 1

r = 7
n = 8
uni = 2


# arr1 = list(map(int, arr.split()))
print(countRats(r,uni, n))