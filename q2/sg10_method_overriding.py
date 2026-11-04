# Super class
class Animal: 
    def __init__(self, name):
        self.name = name

    # Methods to be overridden in child classes
    def eat(self):
        pass

    def make_sound(self):
        pass

# Three sub classes from class Animal
# Methods are overridden whilst inheriting the attributes
class Lion(Animal):

    def eat(self):
        return f"{self.name} eats fresh meat."

    def make_sound(self):
        return f"{self.name} roars loudly!"

class Elephant(Animal):

    def eat(self):
        return f"{self.name} eats grass and fruits."

    def make_sound(self):
        return f"{self.name} trumpets!"

class Monkey(Animal):

    def eat(self):
        return f"{self.name} eats bananas."

    def make_sound(self):
        return f"{self.name} chatters!"

# Instances
lion, elephant, monkey = Lion('Simba'), Elephant('Dumbo'), Monkey('George')

# Output
print(lion.eat())
print(lion.make_sound())
print('-'*5)
print(elephant.eat())
print(elephant.make_sound())
print('-'*5)            
print(monkey.eat())
print(monkey.make_sound())
print('-'*5)