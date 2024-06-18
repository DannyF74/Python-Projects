# Defining parent class
class Vehicle:
    manufacturer = "Unknown"
    color = "unknown"
    land_vehicle = True
    built = 0
    length_mm = 0
    width_mm = 0
    height_mm = 0

    def information(self):
        msg = "\nManufacturer: {}\nColor: {}\nLand Vehicle: {}\nBuilt: {}\nLength (mm): {}\nwidth (mm): {}\nHeight (mm): {}\n".format(self.manufacturer,self.color,self.land_vehicle,self.built,self.length_mm,self.width_mm,self.height_mm)
        return msg

# Defining a child class
class Car(Vehicle):
    manufacturer = "Ford"
    color = "Yellow"
    built = 1972
    length_mm = 4400
    width_mm = 1800
    height_mm = 1800

    def accelerate(self):
        msg = "The car shifts gears and floors it!"
        return msg

# Defining another child class
class Airplane():
    def __init__(self,manufacturer,color):
        self.manufacturer = manufacturer
        self.color = color

    def takeOff(self):
        print("The " + self.color + " " + self.manufacturer + " is taking flight!")
        
if __name__ == "__main__":

    ford = Car()
    print(ford.information())
    print(ford.accelerate())

    a380 = Airplane("Airbus", "white")
    print(a380.takeOff())
    
