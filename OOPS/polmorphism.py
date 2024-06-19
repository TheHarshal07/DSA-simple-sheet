'''
Polymorphism - When the same entity behaves differently in different scenario

for e.g - Water has three state and the behavious in different way for differenct scenario

In programming - 
1 - When same fucntion name use for different types
    e.g print(len("Harry"))
    e.g print(len([10,20,30]))
2- How two different class behvious in same way
'''

class India():
    def capital(self):
        print("Delhi")
    def language(self):
        print("Hindi")

class USA():
    def capital(self):
        print("Washington")
    def language(self):
        print("English")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()