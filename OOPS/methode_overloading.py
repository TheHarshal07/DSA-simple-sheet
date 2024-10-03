'''
Methode overloading - The methode has same name but different signature/parameters

python does not directly support the methode overloading like other languages, It support 
through the various methods

1 - Used the arguments (*args) to make the same function work differently
2 - used None keyword to make the same fucntion work differently
3 - used dispatcher ( from multipledispatch import dispatch)

'''

# 1 - methode
def FirstMethode(datatype, *args):
    if datatype == 'int':
        answer = 0
    
    if datatype == "str":
        answer = ""
    
    for x in args:
        answer = answer + x
    
    print(answer)

FirstMethode('int',5,4)
FirstMethode('str', "Hello", "World")

#2 - SecondMethode using None

def SecondMethode(a=None, b= None):
    if a!= None and b == None:
        print(a)
    else:
        print(a+b)
    
SecondMethode(4)
SecondMethode(4,5)


# 3 - using dispatch ==> Which is most optimal solution

from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    answer =  first * second
    print(answer)

@dispatch(int,int,int)
def product(first, second, third):
    answer = first * second * third
    print(answer)

@dispatch(float,float,float)
def product(first, second, third):
    answer = first*second*third
    print(answer)

product(2,3)
product(2,3,4)
product(2.3,4.1,5.5)