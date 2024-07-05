# Variables
''' 
1. Instance variable - The variables which belongs to the instace/object of that class

2. Class/static variable - The variables which share among all the instances of tha class

'''
class car:

    wheels = 4 # Class variable    

    def __init__(self):
        self.mil = 8
        self.model = "BMW"
    
    def update(self):
        self.mil = 15

c1 = car() # Object is created
c2 = car()

c1.mil = 10             # Upadtes the values
c1.model = "Fortuner" 
c1.update()

car.wheels = 5 # Here I'm changening the value for class variable 

print(c1.mil, c1.model, c1.wheels) 