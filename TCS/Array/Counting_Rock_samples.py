'''
Here we need count the rock samples 
Input: samples[] = {345, 604, 321, 433, 704, 470, 808, 718, 517, 811}, ranges[] = {{300, 380}, {400, 700}}
Output: 2 4
Explanation: 
Range [300, 380]: Samples {345, 321} lie in the range. Therefore, the count is 2. 
Range [400, 700]: Samples {433, 604, 517, 470} lie in the range. Therefore, the count is 4.

'''

def Count_Rock(arr,ranges):
    n = len(arr)
    count = 0
    r = len(ranges)
    c = []
    for i in range(r):
        l,h = ranges[i][0], ranges[i][1] 
        for val in arr:
            if l <= val <= h:
                count += 1
        c.append(count)
    return c


arr = [345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
ranges = [[300, 380],[400,700]]

print(Count_Rock(arr,ranges))