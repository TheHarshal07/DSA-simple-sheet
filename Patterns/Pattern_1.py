'''
Some important things that kept in mind while solving the problems on pattern :
1. For outer loop, focus on no. of lines
2. For inner loop, focus on no. of columns and connect them somehow to the rows
3. print the "*" pattern inside the inner loop
4. Observe Symmestry (Optional) 

'''


def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="") # end is used to add any string at the end of the output in print function 
            # passing whitespace in end parameter indicates that end character has to be identified with whitespace not a new line 
        print("\r")
    
number = int(input("Enter the number :"))
pattern(number)