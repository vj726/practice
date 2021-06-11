#Practice File
#OOPS
#Base class
class Player:
    def __init__(self, name='abc', age=0):
        if age > 18:
            self.name = name
            self.age = age

    def run(self):
        print(f'Player name is {self.name}, age: {self.age}')

    def sign_in(self):
        print('you are signed in')

    def attack(self):
        print('do nothing')

    @classmethod
    def add_num(cls, num1, num2):
        return num1 + num2

    @classmethod
    def create_obj(cls, num1, num2):
        return cls('Chandu', num1 + num2)

    @staticmethod
    def add_num_static(n1, n2):
        return n1 + n2


class Archer(Player):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'{self.name} attacking with {self.arrows} arrows')

#Derived class
class Ranger(Player):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} is attacking with {self.power} power')


# class method example
print(f"class method: {Player.add_num(1, 5)}")

# instantiation using class method
print('\nInstantiation use @class method:')
p3 = Player.create_obj(10, 15)
p3.run()

# static method example
print(f'\n@static method: {Player.add_num_static(10, 40)}')

# Normal instantiation
print('\nNormal instantiation:')
p1 = Archer('Me', 30)
p2 = Ranger("Subha", 60)

p1.attack()
p2.attack()
p1.create_obj(20,12)
