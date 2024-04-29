# Here we need to find out the element which is greater than all of its previous elements
'''
for example:
arr = [ 7,4,8,2,9]
Note: First left most element (7) is always greater than its previous element ( bcz there is no element on left side )

here, 8 > 7,4 ( all its previous elements ) and 9 > (7,4,8,2) ( all its previous element)
'''

def greater_elements(arr):
    n = len(arr)
    max_element = arr[0]
    count = 1  # Bcz first element is always greater than None

    for i in range(1,n):
        if arr[i] > max_element:
            count += 1
            max_element = arr[i]  # Update the max_element
        
    return count

arr = [ 7,4,8,2,9]
print(greater_elements(arr))