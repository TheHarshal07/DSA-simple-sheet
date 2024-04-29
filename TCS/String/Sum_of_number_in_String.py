# Here we have to find the sum of the numbers in String

def Find_Sum(String):

    temp = "0"
    Sum = 0

    for i in range(len(String)):
         if String[i].isdigit():
              temp += String[i]

         else:
              Sum += int(temp)
              temp = "0"

    return Sum + int(temp)

string = "12arshal3Bhogal34"
print(Find_Sum(string))
