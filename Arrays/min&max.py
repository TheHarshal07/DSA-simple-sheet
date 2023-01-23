#Here we need to find the max and min elements in the array 

l = [10,20,2,60,35]

max = l[0]
min = l[0]

for i in range(len(l)):
    if l[i] > max:
        max = l[i]
    elif l[i] < min:
        min = l[i]

print("Minimum element is " f'{min}' " and Maximum element is " f'{max}')
 