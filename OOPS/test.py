
def smallnumber(arr,sum):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if((arr[i]+arr[j]+arr[k])<sum):
                    count += 1
    return count

arr = [5,1,3,4,7]
sum = 12 
print(smallnumber(arr,sum))
