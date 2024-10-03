'''
Methode overriding - The methode has same name and same parameter

'''

class Animal:
    def sound(self):
        return "Lion roaring"

class Dog(Animal):
    def sound(slef):
        return "dog barking"

class Cat(Animal):
    def sound(self):
        return "Cat meow"
    
dog = Dog()
cat = Cat()
animal =  Animal()

print(animal.sound())
print(dog.sound())
print(cat.sound())