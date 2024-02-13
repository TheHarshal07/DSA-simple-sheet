# In thi problem you have determine the best time to buy and sell the stock
# Note : if you sell stock on the ith day you buy the stock on minimum prices from (i-1)

def BestTimeToBuyandSell(arr,n):
    mini = arr[0]
    profit = 0
    for i in range(1,n):
        cost = arr[i] - mini 
        profit = max(profit, cost)
        mini = min(mini, arr[i])
    return (mini,arr[i])

arr = [7,1,3,4,6,5]
n = len(arr)
print(BestTimeToBuyandSell(arr,n))




def BestTime(arr,n):
    mini = arr[0]
    profit = 0
    for i in range(1,n):
        cost = arr[i] - mini
        profit = max(profit, cost)
        mini = min(mini,arr[i])
    return profit

arr = [6,2,5,1,7]
n = len(arr)
# print(BestTime(arr,n))