''' 
Call by refrence - Here we pass the memory address of the original data to the function
so if any changes made in function it will reflect to the original data

It is useful when we don't want the function to change the original data
'''

def add(x):
    x.append(1)
    return x

num = [1]
print(add(num))


'''
Call by value - Here we pass the copy of the original data to the function
so if any changes made in function it will not get reflect into the original data

It is usefull when want the function need to change the original data
'''

def addd(x):
    return x+1

num = 2
print(addd(2))