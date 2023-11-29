'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA

Here we have to break the increment order from the middle
Breakoint is - (2*i+1)/2

'''

def pattern_16(n):
    for i in range(0, n):
        
        #space
        for j in range(n-i-1):
            print(" ", end="")
            
        #alphabet
        breakpoints = (2*i+1) / 2
        char = "A"
        for k in range(2*i+1):
            print(char, end="")
            if (k <= breakpoints):
                char = chr(ord(char)+1)
            else:
                char = chr(ord(char)-1)
        #space
        for l in range(n-i-1):
            print(" ",end="")

        print("\r")

n = 5
pattern_16(n)