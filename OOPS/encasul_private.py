''' Here we gonna implement encapsulation as private memeber '''


# Encapsulation as private member - We can access it from own class and derived class but we couldn't access it 
                                    # from object

# Here we have access the private member using Own class
class Encapsule:
    def __init__(self,name, age):
        self.__name = name
        self.__age = age
        print(self.__name)
        print(self.__age)

obj = Encapsule("Harshal",21)
# print(obj.name, obj.age)    <<-- This is will lead to the error, bcz we are accessing private class from the outside the class


''' WE can access the private class fromt followintg two methods
    1. public methode to acess the private members
    2. name mangling to acess the private members  - it make use of single underscore to access 
'''

# This is public methode to access the private members
class Encap:
    _name = "Rohit"
    _age = 20
class dervied(Encap):
        def __init__(self):
            print(self._name)
            print(self._age)

objj = dervied()


# 2. This is name mangling to acess the private members

class Encap:
    _name = "Rohit"
    _age = 20
class dervied(Encap):
        def __init__(self):
            print(self._name)
            print(self._age)

objj = dervied()
print("name {}, age {}".format(objj._name, objj._age))  # <<--- Name mangling to access the private members   
