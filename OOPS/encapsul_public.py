''' 
Here we gonna implement Encapsulation concept

'''


# This is example of encapsulation as public member
class encapsul:
    #constructor
    def __init__(self,name="Harry",age="25"):
        self.name = name
        self.age = age

obj = encapsul()
obj2 = encapsul("Harshal",21)
# obj()
print("Name {}, age {}".format(obj.name, obj.age))
print("Name {}, age {}".format(obj2.name, obj2.age))
