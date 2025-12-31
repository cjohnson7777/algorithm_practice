from abc import ABC, abstractmethod

# ABSTRACT PRODUCT

# Window
class Window(ABC):
    @abstractmethod
    def create_window(self):
        pass

# Button
class Button(ABC):
    @abstractmethod
    def create_button(self):
        pass

# CONCRETE PRODUCT

# Window's Window
class WindowsWindow(Window):
    def create_window(self):
        return "Window's Window"

# Window's Button
class WindowsButton(Button):
    def create_button(self):
        return "Window's Button"

# MacOS Window
class MacOSWindow(Window):
    def create_window(self):
        return "Mac Window"
    
# MacOS Button
class MacOSButton(Button):
    def create_button(self):
        return "Mac Button"

# ABSTRACT FACTORY
class Factory(ABC):
    @abstractmethod
    def getWindow(self):
        pass

    @abstractmethod
    def getButton(self):
        pass
        
# CONCRETE FACTORY

# Windows UI Factory
class WindowsFactory(Factory):
    def getWindow(self):
        return WindowsWindow()
        
    def getButton(self):
        return WindowsButton()

# MacOS UI Factory
class MacOSFactory(Factory):
    def getWindow(self):
        return MacOSWindow()
        
    def getButton(self):
        return MacOSButton()
    
# Client Code

def build_popup(factory):
    window = factory.getWindow()
    button = factory.getButton()

    print(window.create_window())
    print(button.create_button())

build_popup(MacOSFactory())
build_popup(WindowsFactory())


