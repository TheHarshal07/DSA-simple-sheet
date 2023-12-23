'''
Reverse the number:
input - 7789
output - 9877

'''
def reverse_number(arr):
    start = 0
    end = len(arr)-1

    while(start< end):
        arr[start], arr[end] = arr[end],arr[start]
        start += 1
        end -=1
    return arr

arr = [4,3,2,1]
print(reverse_number(arr))




def reverse(num):
    reverNumber = 0
    temp = num
    while(num>0):
        lastdigit = num % 10
        num //= 10
        reverNumber = (reverNumber * 10) + lastdigit
        
    # if reverNumber == temp: return True
    # else: return False
    return reverNumber
    

arr = 87654
print(reverse(arr))