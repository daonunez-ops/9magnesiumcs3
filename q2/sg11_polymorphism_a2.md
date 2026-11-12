# 1. Answer the following questions:

## a. What is duck typing, as explained in the video?
### **Duck Typing is a perception that views an object base on what they have and act. An example of duck typing is labelling a pronghorn an antelope despite it being closer to a giraffe.**

## b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
### **The Car must have a similar behaviour or similar attributes relative to the Animal Class to look as if the car is from an Animal.**

# 2. Create the Python code that:
## a. Creates three classes: Car, Boat, and Drone with a method move().
## move() in the Car class prints "The car drives on the road."
## move() in the Boat class prints "The boat sails on water."
## move() in the Drone class prints "The drone flies in the sky."
## b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().
## c. Creates one object of each class.
## d. Calls the start_trip() method for each object.

### [**--> Code**](q2/sg11_polymorphism_a2.py)

# 3. How does the code in 2.2 demonstrate polymorphism?
### **It demonstrates polymorphism through duck typing because the classes did not inherit attributes from a possible vehicle class and it's not a built-in function either. Another reason why it demonstrates duck typing because each vehicle have similar methods.**