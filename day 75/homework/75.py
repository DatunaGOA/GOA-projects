# Base Class (Root)
class LivingBeing:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"{self.name} is a living being."

# First Level Classes
class Animal(LivingBeing):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def description(self):  
        return f"{self.name} is an animal that lives in {self.habitat}."

class Plant(LivingBeing):
    def __init__(self, name, type_of_plant):
        super().__init__(name)
        self.type_of_plant = type_of_plant

    def description(self):  
        return f"{self.name} is a {self.type_of_plant} plant."

# Second Level Classes
class Mammal(Animal):
    def __init__(self, name, habitat, warm_blooded):
        super().__init__(name, habitat)
        self.warm_blooded = warm_blooded

    def description(self):  
        return f"{self.name} is a mammal that lives in {self.habitat} and is {'warm-blooded' if self.warm_blooded else 'not warm-blooded'}."

class Bird(Animal):
    def __init__(self, name, habitat, can_fly):
        super().__init__(name, habitat)
        self.can_fly = can_fly

    def description(self):  
        return f"{self.name} is a bird that lives in {self.habitat} and {'can fly' if self.can_fly else 'cannot fly'}."

class FloweringPlant(Plant):
    def __init__(self, name, type_of_plant, flower_color):
        super().__init__(name, type_of_plant)
        self.flower_color = flower_color

    def description(self):  
        return f"{self.name} is a {self.type_of_plant} that has {self.flower_color} flowers."

class NonFloweringPlant(Plant):
    def __init__(self, name, type_of_plant):
        super().__init__(name, type_of_plant)

    def description(self):  
        return f"{self.name} is a {self.type_of_plant} that does not have flowers."

# Third Level Class
class Dog(Mammal):
    def __init__(self, name, habitat, warm_blooded, breed):
        super().__init__(name, habitat, warm_blooded)
        self.breed = breed

    def description(self): 
        return f"{self.name} is a {self.breed} dog, a warm-blooded mammal that lives in {self.habitat}."
