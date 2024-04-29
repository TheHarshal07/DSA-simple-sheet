# Here we have to convert the Decimal to Binary

def Conversion(num):
    
    if num >= 1:
        Conversion(num//2)
        print(str(num%2), end="")


def Built_in_methode(num):
    binary = format(num,'b')
    print(binary, end="")

Conversion(10)
Built_in_methode(10)