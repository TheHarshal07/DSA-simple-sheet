r = int(input("enter the number :"))

for i in range(r):
    for j in range(i+1):
        print(j+1,end="")
    print("\r")