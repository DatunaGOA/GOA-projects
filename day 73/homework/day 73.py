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
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"




















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
    def charge(self):
        return "Charging..."

class SportsCar(Car):
    def race(self):
        return "Vroom!"











class Person:
    population = 0  # Static variable to count population

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def get_name(self):
        return self.name

    @classmethod
    def get_population(cls):
        return cls.population

class Student(Person):
    def study(self):
        return "Studying..."

class Teacher(Person):
    def teach(self):
        return "Teaching..."


















class Library:
    book_count = 0  # Static variable to count books

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
