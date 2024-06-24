# Here we are importing the abstract methods from the ABC library in Python
from abc import ABC, abstractmethod

# Here we are creating a parent class called firework and creating a launch method
# which all fireworks will use. We then create two abstract methods that will need
# to be defined by each child firework as they will need different information.
# We impliment this here because all child objects will need to use these methods.
class firework(ABC):
    def launch(self, amount):
        print("\n\nPreparing to launch " + str(amount) + " fireworks.")
    
    @abstractmethod
    def explosion(self, amount):
        pass
    
    @abstractmethod
    def color(self, color):
        pass

# Here we create some child objects and define the abstract methods listed in the parent.
# We give each child object their specific behaviors in their definitions.

class big_blue_firework(firework):
    def explosion(self, amount):
        print("The " + str(amount) + " big fireworks boom in the sky!")
    
    def color(self, color):
        print("They sparkle with a " + color + " glow!")

class catherine_wheel(firework):
    def explosion(self, amount):
        print("The " + str(amount) + " catherine wheels fire up and spin faster and faster")
    
    def color(self, color):
        print("The rockets spit out " + color + " sparks!")

# Here we instantiate two fireworks from the two child classes. We then call the methods
# from the parent class and the child class. We can see when this is run, although the
# same name of method is called, the output is taken from the corresponding child class.

firework1 = big_blue_firework()
firework1.launch(5)
firework1.explosion(5)
firework1.color("blue")

firework2 = catherine_wheel()
firework2.launch(2)
firework2.explosion(2)
firework2.color("orange")