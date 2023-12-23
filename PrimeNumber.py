# Here we will gonna check wether the num is prime num or not

def isPrime(num):
    if(num==0 or num==1):
        print(f"{num} is not prime number")
        
    if (num==2):
        print(f"{num} is prime number ")
    for i in range(2, num):
        if (num % i == 0):
            print(f"{num} is not prime number ")
            break
        else:
            print(f"{num} is the prime number ")
            break
    


num = int(input("Enter the num :"))
isPrime(num)