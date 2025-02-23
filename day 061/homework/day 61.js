// Task 1:
const person = {
    name: "Davit",
    age: 14,
    city: "Kareli"
};

// Task 2: 
const car = {
    make: "Toyota",
    model: "Camry",
    year: 2021
};
console.log(`Make: ${car.make}, Model: ${car.model}, Year: ${car.year}`);

// Task 3: 
person.age = 31; 
console.log(`Updated Age: ${person.age}`);

// Task 4:
person.hobby = "Reading"; 
console.log(`Hobby: ${person.hobby}`);

// Task 5: 
delete person.city; 
console.log(`Person after deleting city:`, person);

// Task 6: 
const calculator = {
    a: 5,
    b: 10,
    add: function() {
        return this.a + this.b;
    }
};
console.log(`Sum: ${calculator.add()}`);

// Task 7: 
const book1 = { title: "1984", author: "George Orwell", pages: 328 };
const book2 = { title: "To Kill a Mockingbird", author: "Harper Lee", pages: 281 };
const book3 = { title: "The Great Gatsby", author: "F. Scott Fitzgerald", pages: 180 };

// i just searched up books cuz i dont read books :)

console.log(`Books:`, book1, book2, book3);

// Task 9:
function Animal(name, sound) {
    this.name = name;
    this.sound = sound;
    this.makeSound = function() {
        console.log(`${this.name} says: ${this.sound}`);
    };
}

// Task 10: 
const cat = new Animal("Cat", "Meow");
const dog = new Animal("Dog", "Woof");
cat.makeSound();
dog.makeSound();

// Task 11: 
Animal.prototype.changeName = function(newName) {
    this.name = newName;
};

cat.changeName("Kitty");
dog.changeName("Buddy");
cat.makeSound();
dog.makeSound();
