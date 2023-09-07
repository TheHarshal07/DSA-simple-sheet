'''
    *
   ***
  *****
 *******
*********

'''
def StarPattern(n):
    for i in range(n):
        #space
        for j in range(n-i-1):
            print(" ", end="")
        #stars
        for k in range(2*i+1):
            print("*", end="")
        #space
        for l in range(n-i-1):
            print(" ", end="")
        print("\r")

Number = int(input("Enter the number :"))
StarPattern(Number)
        

