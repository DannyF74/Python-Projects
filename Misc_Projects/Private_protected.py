class protected:
    def __init__(self):
        self._protectedVar = 0

class private:
    def __init__(self):
        self.__privateVar = 123

    def getNumber(self):
        print(self.__privateVar)

    def setNumber(self, number):
        self.__privateVar = number

test = protected()
test._protectedVar = 1
print(test._protectedVar)

test2 = private()
test2.getNumber()
test2.setNumber(1234)
test2.getNumber()

