class Animal:
    species_count = 0  

    def __init__(self, name):
        self.name = name
        Animal.species_count += 1

    def get_name(self):
        return self.name

    @classmethod
    def get_species_count(cls):
        return cls.species_count

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        return "Woof!"

    def get_breed(self):
        return self.breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        return "Meow!"

    def get_color(self):
        return self.color















class Car:
    car_count = 0  

    def __init__(self, model):
        self.model = model
        Car.car_count += 1

    def get_model(self):
        return self.model

    @classmethod
    def get_car_count(cls):
        return cls.car_count

class ElectricCar(Car):
    def __init__(self, model, battery_size):
        super().__init__(model)
        self.battery_size = battery_size

    def charge(self):
        return "Charging..."

    def get_battery_size(self):
        return self.battery_size

class SportsCar(Car):
    def __init__(self, model, top_speed):
        super().__init__(model)
        self.top_speed = top_speed

    def race(self):
        return f"Racing at {self.top_speed} mph!"

    def get_top_speed(self):
        return self.top_speed















class Person:
    population = 0  

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def get_name(self):
        return self.name

    @classmethod
    def get_population(cls):
        return cls.population

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def study(self):
        return f"Studying {self.major}."

    def get_major(self):
        return self.major

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def teach(self):
        return f"Teaching {self.subject}."

    def get_subject(self):
        return self.subject

# Bonus Class: Library
class Library:
    book_count = 0 

    def __init__(self, name):
        self.name = name
        Library.book_count += 1

    def get_name(self):
        return self.name

    @classmethod
    def get_book_count(cls):
        return cls.book_count

class PublicLibrary(Library):
    def open(self):
        return "Library is open!"

class PrivateLibrary(Library):
    def close(self):
        return "Library is closed!"

