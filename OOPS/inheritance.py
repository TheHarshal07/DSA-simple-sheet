
''' 
This is example of inheritance:
1. Single inheritance
2. multi-level inheritance
3. multiple inheritance
'''

class Animal:
    def bark(self):
        print("Dogg is barking")

class cat(Animal):  # single inheritance
    def meow(self):
        print("Cat is meowing")

class dog(cat):     # Multi-level inheritance - Derived class inherti the property of another derived class
    def dogs(self):
        print("dog are good")

obj = dog()
obj.bark()
obj.meow()
obj.dogs()



'''
Multiple inheritance

'''

class Computer:
    def cpu(self):
        print("intel i5")

class Mobile:
    def company(self):
        print("Samsung")
    
class Tablet:
    def battery(self):
        print("5400mh")

class Tech(Computer, Mobile, Tablet):
    def technologies(self):
        print(" THis are the technologies ")


t = Tech()
t.technologies()
t.cpu()
t.battery()
t.company()
