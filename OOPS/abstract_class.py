'''
Here we gonna creating abstract class 

Here we have use abc module to create the abstract base class, and then we created Car class that inherit the 
ABC class and define abstract methode.

Some Important point to note it down:
1. An abstract class contain both methode normal and abstract methode
2. An abstract cannot be instantiated, and we cannot create the object of abstract class

'''

from abc import ABC, abstractmethod

class Car(ABC):  # <<--- Abstract class
    def milegae(self):
        pass

class swift(Car):
    def milage(self): # abstract methode
        print("The milage is 40km/hr")

class Tesla(Car):
    def milage(self):
        print("The milage us 30km/hr")

class Hundai(Car):
    def milage(self):
        print("The milage is 30km/hr ")


s = swift()
s.milage()

T = Tesla()
T.milage()

H = Hundai()
H.milage()
