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

print("----------- sort the array -----------------")

def sort(arr):
    result = []
    for i in range(len(arr)-1 ,-1,-1):
        result.append(arr[i])

    return result

arr = [ 4,3,2,1]
print(sort(arr))



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