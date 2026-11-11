class Car: # Independent Class
    def move(self): # Defines its own move method
        return 'The car drives on the road.' # Returns a string

class Boat: # Independent Class
    def move(self): # Defines its own move method
        return 'The boat sails on water.' # Returns a string

class Drone: # Independent Class
    def move(self): # Defines the move method
        return 'The drone flies in the sky.' # Returns a string

def start_trip(vehicle): # Function to associate the move method of the object passed as an argument
    print(vehicle.move()) # Calls the move method of the object

# Instances
c, b, d = Car(), Boat(), Drone()

# Call them on state
start_trip(c), start_trip(b), start_trip(d)