#here we gonaa implement stack 

stack = []

def StackImplementation(arr):
    for i in range(len(arr)):
        stack.append(arr[i])
    
    print("Initial stack",stack)

    print(stack.pop())
    print(stack.pop())
    print("Stack after poping", stack)

arr = [ 1,2,3,4]
StackImplementation(arr)