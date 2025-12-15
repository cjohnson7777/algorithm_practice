from abc import ABC, abstractmethod

# DISPLAY STRATEGIES
class DisplayStrategy(ABC):
    @abstractmethod
    def display(self):
        pass

# Simple Display
class SimpleDisplayStrategy(DisplayStrategy):
    def display(self):
        print("Simple Duck Display")

# QUACK STRATEGIES
class QuackStrategy(ABC):
    @abstractmethod
    def quack(self):
        pass

# City Quack
class CityQuackStrategy(QuackStrategy):
    def quack(self):
        print("City Quack")

# Farm Quack
class FarmQuackStrategy(QuackStrategy):
    def quack(self):
        print("Farm Quack")

# FLY STRATEGIES
class FlyStrategy(ABC):
    @abstractmethod
    def fly(self):
        pass

# No Fly
class NoFlyStrategy(FlyStrategy):
    def fly(self):
        print("Can't Fly")

# High Fly
class HighFlyStategy(FlyStrategy):
    def fly(self):
        print("High Fly")

# Low Fly
class LowFlyStategy(FlyStrategy):
    def fly(self):
        print("Low Fly")

# DUCK CLASS
class Duck:
    def __init__(self, display, quack, fly):
        self._display = display
        self._quack = quack
        self._fly = fly

    def duck_display(self):
        self._display.display()

    def duck_quack(self):
        self._quack.quack()

    def duck_fly(self):
        self._fly.fly()

duck = Duck(SimpleDisplayStrategy(), CityQuackStrategy(), HighFlyStategy())
duck.duck_display()


