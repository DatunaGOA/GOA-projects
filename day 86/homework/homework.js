// 1) 
let countryCapitalMap = new Map();
countryCapitalMap.set('Georgia', 'Tbilisi');
countryCapitalMap.set('France', 'Paris');
countryCapitalMap.set('Japan', 'Tokyo');
countryCapitalMap.forEach((capital, country) => {
    console.log(`${country}: ${capital}`);
});

// 2) 
let cityMap = new Map();
cityMap.set('Tbilisi', 'Capital of Georgia');
cityMap.set('Paris', 'Capital of France');
cityMap.set('Tokyo', 'Capital of Japan');
console.log(cityMap.has('Tbilisi')); 
console.log(cityMap.has('Berlin'));  

// 3) 
let studentGrades = new Map();
studentGrades.set('Alice', 95);
studentGrades.set('Bob', 85);
studentGrades.set('Charlie', 78);
console.log(studentGrades.get('Bob')); 

// 4) 
let countryMap = new Map();
countryMap.set('Georgia', 'Tbilisi');
countryMap.set('France', 'Paris');
countryMap.set('Japan', 'Tokyo');
for (let country of countryMap.keys()) {
    console.log(country);
}

// 5) 
let myMap = new Map();
myMap.set('city', 'Tbilisi');
myMap.set('country', 'Georgia');
myMap.set('capital', 'Tbilisi');
myMap.delete('city');
myMap.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});

// 6) 
let productMap = new Map();
productMap.set('Laptop', 1000);
productMap.set('Phone', 500);
productMap.set('Tablet', 300);
console.log(productMap.size); 

// 7) 
let priceMap = new Map();
priceMap.set('Apple', 1.5);
priceMap.set('Banana', 0.5);
priceMap.set('Orange', 2);
priceMap.set('Banana', 0.75);
priceMap.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});

// 8) 
let emptyMap = new Map();
console.log(emptyMap.size === 0); 

// 9) 
let productObj = {
    'Laptop': 1000,
    'Phone': 500,
    'Tablet': 300
};
let objToMap = new Map(Object.entries(productObj));
objToMap.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});

// 10) 
let dataMap = new Map();
dataMap.set('Item1', 100);
dataMap.set('Item2', 200);
dataMap.set('Item3', 300);
dataMap.clear();
console.log(dataMap.size === 0); 
