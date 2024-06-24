# This creates a protected class and sets its initial value to 0
class protected:
    def __init__(self):
        self._protectedVar = 0

# This creates a private class and sets its initial value to 123.
# Then creates some methods to allow the values to be viewed and changed
class private:
    def __init__(self):
        self.__privateVar = 123

    def getNumber(self):
        print("privateVar = " + str(self.__privateVar))

    def setNumber(self, number):
        self.__privateVar = number

# This creates an instance of the protected class named test. Then sets the value
# of the protected var in the object to 1 and then prints the protected var as a string
test = protected()
test._protectedVar = 1
print("protectedVar = " + str(test._protectedVar))


# This creates an instance of the private class named test2. Runs the getNumber method
# to show what the value is initially set to as a string. Then runs the set number method
# to change the value of the variable to 1234. Finally runs the getNumber method
# again to print the new value in the private var as a string. 
test2 = private()
test2.getNumber()
test2.setNumber(1234)
test2.getNumber()

