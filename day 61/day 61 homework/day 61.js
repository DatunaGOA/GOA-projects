
let person = {
    name: "John",
    age: 30,
    city: "New York"
};




let car = {
    make: "Toyota",
    model: "Corolla",
    year: 2020
};


console.log(car.make);  
console.log(car.model); 
console.log(car.year); 



person.age = 35;
console.log(person.age); 



person.hobby = "Reading";
console.log(person.hobby);



delete person.city;
console.log(person.city); 



let calculator = {
    a: 5,
    b: 10,
    add: function() {
        return this.a + this.b;
    }
};


console.log(calculator.add());



let book1 = {
    title: "1984",
    author: "George Orwell",
    pages: 328
};

let book2 = {
    title: "To Kill a Mockingbird",
    author: "Harper Lee",
    pages: 281
};

let book3 = {
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    pages: 180
};


console.log(book1.title, book1.author, book1.pages);
console.log(book2.title, book2.author, book2.pages);
console.log(book3.title, book3.author, book3.pages);



function Animal(name, sound) {
    this.name = name;
    this.sound = sound;
    this.makeSound = function() {
        console.log(this.sound);
    };
}



Animal.prototype.changeName = function(newName) {
    this.name = newName;
};


cat.changeName("Kitty");
console.log(cat.name);


