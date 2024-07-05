
'''

THere are two methods to acess the private members
1. Public methods to acess the private members
2. name managling to acess the private members
'''

class Encaps:
    _name = "Harshal"
    _age = 21

class derived(Encaps):
    def __init__(self):
        print(self._name)
        print(self._age)

obj = derived()


class Encps:
    _name = "Rohit"
    _age = 20

class derive(Encps):
    def __init__(self):
        self._name
        self._age

obj = derive()
print("namne {} and age {}".format(obj._name, obj._age))