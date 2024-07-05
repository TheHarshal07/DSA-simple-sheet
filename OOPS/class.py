# What is class ?
'''
Class is the blueprint from which an object is created 
It has methode and variables
Inside the class we write the design of the objet
'''
# What is Object ?
'''
Object is an instance of the class
it has state and behavoir 
'''

class computer:

    def __init__(self):
        self.name = "Harshal"
        self.age = 21
    
    def name1(self):
        print(self.name, self.age)


    def config(self): # self is object we are passing basicallu it points the object/instance
        print("Intel, i5 processor, 8Gb")

c1 = computer() # Object is created
c2 = computer()
c1.name1()
