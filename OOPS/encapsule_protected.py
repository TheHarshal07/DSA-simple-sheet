'''
Here we implement the encapsulation in using protected member

Note:
TO spcify the protected access modifier of member, we make as use of underscore - _
'''

class encapsul:
    _name = "Sanika"
    _age = 18

class derived(encapsul):
    def __init__(self):
        print(self._name)
        print(self._age)

obj = derived()
# print(obj.name) <<-- THis give me error
print(obj._name)  # << Name mangling to access the protected member