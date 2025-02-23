const bookstore = new Map([
    ["001", { title: "ფიქრის მექანიკა", author: "პეტრე სულამიძე", genre: "ფილოსოფია", price: 25, status: "available" }],
    ["002", { title: "სამყაროს საიდუმლოებები", author: "მარიამ გაბუნია", genre: "მეცნიერება", price: 30, status: "available" }],
]);

const personalCollection = new Map();

function addToCollection(id) {
    if (bookstore.has(id) && bookstore.get(id).status === "available") {
        personalCollection.set(id, { ...bookstore.get(id), status: "added" });
        bookstore.get(id).status = "added";
        console.log(`"${bookstore.get(id).title}" დამატებულია კოლექციაში.`);
    }
}

function removeFromCollection(id) {
    if (personalCollection.has(id)) {
        bookstore.get(id).status = "available";
        personalCollection.delete(id);
        console.log(`"${id}" წაშლილია კოლექციიდან.`);
    }
}

function searchBooks(query) {
    console.log(Array.from(bookstore.values()).filter(book => book.title.includes(query) || book.author.includes(query)));
}




//console.log: Outputs a message to the browser’s console, often used for debugging or showing information.

// Example: console.log("Hello, World!");
// const: Declares a block-scoped, read-only variable. The value cannot be reassigned, but objects it references can be mutated.

// Example: const name = "Alice";
// .filter(): Creates a new array with elements that satisfy a condition defined in a callback function.

// Example: [1, 2, 3].filter(n => n > 1); // [2, 3]
// Map: A collection of key-value pairs where keys can be any type. It provides methods like .set(), .get(), and .has().

// Example: const myMap = new Map(); myMap.set("key", "value");
// .set(): Adds or updates a key-value pair in a Map.

// Example: myMap.set("color", "blue");
// if: Executes a block of code only if a specified condition evaluates to true.

// Example:
// if (age > 18) {
//     console.log("Adult");