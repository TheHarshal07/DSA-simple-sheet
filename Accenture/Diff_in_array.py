'''
int findCount(int arr[], int length, int num, int diff);

The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’.
Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.

Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.


Input:

arr: 12 3 14 56 77 13
num: 13
diff: 2

Output:
3

'''

def findCount(num,diff):
    arr = [12,3,14,56,77,13]
    count = 0
    for i in range(len(arr)):
        if (abs(arr[i]-num)<=diff):
            count+= 1
    if count:
        return count
    return 0 

num = 13
diff = 2
print(findCount(num,diff))
