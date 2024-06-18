

# Creating the parent class using the __init__ method so we can provide the information
# when instantiating the user
class User:
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password

# The below function was just to test that the user had been created properly
    def printname(self):
        print(self.fname, self.lname)
            
# Creating a login method to allow users to log in. They must enter their username
# and password correctly.
    def login(self):
        user_login = input("Please enter your username: ")
        user_password = input("Please enter your password: ")
        if (user_login == self.username and user_password == self.password):
            print("Welcome back, {} {}.".format(self.fname,self.lname))
        else:
            print("The login information you've provided is incorrect. Please try again")

# Creating a child class which uses a pin number rather than a password.
class Nurse(User):
    def __init__(self, fname, lname, username, pin_number):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.pin_number = pin_number
 
# Here we are copying the function above but if the user is a nurse, they must use
# a pin number rather than a password.
    def login(self):
        user_login = input("Please enter your username: ")
        user_pin = input("Please enter your pin number: ")
        if (user_login == self.username and user_pin == self.pin_number):
            print("Welcome back, Nurse {}.".format(self.lname))
        else:
            print("The login information you've provided is incorrect. Please try again")

# Creating another child class. Here we are adding additional bits of info to make the
# login method below more secure.
class Doctor(User):
    def __init__(self, fname, lname, username, license_number, pin_number):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.license_number = license_number
        self.pin_number = pin_number

    
# Here we are copying the function above but if the user is a doctor, they must provide
# a pin number rather than a password and give their license number.
    def login(self):
        user_license = input("Please enter your license number: ")
        user_login = input("Please enter your username: ")
        user_pin = input("Please enter your pin number: ")
        if (user_license == self.license_number and user_login == self.username
            and user_pin == self.pin_number):
            print("Welcome back, Doctor {}.".format(self.lname))
        else:
            print("The login information you've provided is incorrect. Please try again")

# Below we are creating a new user and a new doctor and testing our polymorphed methods.
if __name__ == "__main__":
    user1 = User("John","Adams","jadams","password")
    user1.printname()
    user1.login()
    nurse1 = Nurse("Julia", "Francis", "jfrancis", "1234")
    nurse1.printname()
    nurse1.login()
    doctor1 = Doctor("James", "Smith", "jsmith", "001", "123456")
    doctor1.printname()
    doctor1.login()
        
