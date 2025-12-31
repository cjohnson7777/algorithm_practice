from abc import ABC, abstractmethod

# SUBJECT (OBSERVABLE)

class Subject(ABC):
    @abstractmethod
    def add(observer):
        pass
    
    @abstractmethod
    def remove(observer):
        pass

    @abstractmethod
    def notify():
        pass

# OBSERVER
class Observer(ABC):
    def update(self):
        pass

# CONCRETE OBSERVABLE
# Weather Station
class WeatherStation(Subject):
    def __init__(self, temperature):
        self.observers = []
        self.temperature = temperature
    
    def add(self, observer):
        self.observers.append(observer)
    
    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def updateTemperature(self, newTemp):
        self.temperature = newTemp

    def getTemperature(self):
        return self.temperature

# CONCRETE OBSERVER  
# Displays
class Displays(Observer):
    def __init__(self, subject):
      self.subject = subject

    def update(self):
        print(self.subject.getTemperature())

weather = WeatherStation(9)
phone = Displays(weather) 
weather.add(phone)
weather.notify()
weather.updateTemperature(34)
weather.notify()