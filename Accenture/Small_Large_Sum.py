''''
Here we have to find out the second largest number from even and odd position in the array
at the end we have to add them and return

input : 
arr = [ 3,1,2,5,7,9]
output: 8

Here, odd postion are - 1,5,7 so, 5 is the second largest number
      even postion are - 3,2,9 so, 3 is the second largest number
      addition of 3 and 5 is 8

'''

def SmallLargeSum(arr,n):
    evenLargest = arr[0]
    oddlargest = arr[1]
    for i in range(n):
        if (i % 2 == 0):
           
            if arr[i]>evenLargest:
                evenSecondLargest = evenLargest
                evenLargest = arr[i]
        else:
            if arr[i] > oddlargest:
                oddsecondlargest = oddlargest
                oddlargest = arr[i]
    sum = evenSecondLargest + oddsecondlargest
    return sum


arr = [3,1,2,5,7,9]
l = len(arr)
print(SmallLargeSum(arr,l))
