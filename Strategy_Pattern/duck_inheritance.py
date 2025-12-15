### USING INHERITANCE

# DUCK CLASS
class Duck:
    def __init__(self):
        pass

    def duck_display(self):
        print("Display")

    def duck_quack(self):
        print("Quack")

    def duck_fly(self):
        print("fly")

# CITY DUCK CLASS  
class CityDuck(Duck):
    def __init__(self):
        super().__init__()
    
    def high_fly(self):
        print("High Fly")

duck = CityDuck()
duck.high_fly()