# Types of methods
'''
1. Instance methods - It works with instance variable
2. class methdos    - It works with class variable
3. Static methods   - It works with nothing ( If you want extra stuff)

'''
class students:
    school = "Harry's School"

    def __init__(self,m1,m2,m3):  # Instance methdos
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    @classmethod               # This is decorators - It improves the functionality of the existing function
    def getschool(cls):
        return cls.school 
    
    @staticmethod
    def info():
        print("This is information about this class!")


    def avg(self):
        return (self.m1+self.m2+self.m3)/3

obj1 = students(10,20,30)
obj2 = students(50,60,70)

print(obj1.avg())
print(obj2.avg())

print(students.getschool())  # This is class methods 
students.info()


