'''
Here we have given a string 
string = harshal.sudhir.bhogal
output = bhogal.sudhir.harshal

'''
def ReverseString(str):
    string = str.split(".")
    print(string)
    n = len(string)
    temString = ""
    for i in range(n-1,-1,-1):
        if (i!=0):
            temString = temString+string[i]+"."
            # print(temString)
        else:
            temString = temString+string[i]
            
    return temString

s = "harshal.sudhir.bhogal"
print(ReverseString(s))
