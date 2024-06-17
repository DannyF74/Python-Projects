
# creating a new class called vehicle.
class vehicle:
    manufacturer = 'No manufacturer provided'
    model = 'No model provided'
    year = 0

# Creating child classes with unique attributes to their classes.

class boat(vehicle):
    sails = 'no sail information'
    hull_material = 'No hull information'

class car(vehicle):
    drivetrain: 'No drivetrain information'
    trunk_capacity = 0
    
