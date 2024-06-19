#here we gonna implement fibonacci series using recurion

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

num = 5
for i in range(num):
    print("Fibonacci series ", fibonacci(i))