let n = Number(prompt("Enter arr length: "))
let arr = []
for(let i=0; i<n; i++){
    arr.push(Number(prompt("Enter number :")))
}


// 1. for ციკლი - რიცხვების დიაპაზონის გავლა
console.log("for ციკლი:");
for (let i = 0; i < 5; i++) {
    console.log(i);  // Output: 0, 1, 2, 3, 4
}

// 2. forEach() - მასივის ელემენტებზე მუშაობა
console.log("\nforEach() ფუნქცია:");
let fruits = ['apple', 'banana', 'cherry'];
fruits.forEach(function(fruit, index) {
    console.log(index, fruit);  // Output: 0 'apple', 1 'banana', 2 'cherry'
});

// 3. map() - ახალი მასივის შექმნა
console.log("\nmap() ფუნქცია:");
let numbers = [1, 2, 3, 4];
let squaredNumbers = numbers.map(function(number) {
    return number * number;  // Output: [1, 4, 9, 16]
});
console.log(squaredNumbers);

// 4. filter() - ფილტრაცია
console.log("\nfilter() ფუნქცია:");
let numbers2 = [1, 2, 3, 4, 5];
let evenNumbers = numbers2.filter(function(number) {
    return number % 2 === 0;  // Output: [2, 4]
});
console.log(evenNumbers);

// 5. reduce() - ელემენტების შეკუმშვა
console.log("\nreduce() ფუნქცია:");
let numbers3 = [1, 2, 3, 4];
let sum = numbers3.reduce(function(accumulator, currentValue) {
    return accumulator + currentValue;  // Output: 10
}, 0);  // accumulator starts from 0
console.log(sum);

// 6. concat() - მასივების შეერთება
console.log("\nconcat() ფუნქცია:");
let array1 = [1, 2];
let array2 = [3, 4];
let combined = array1.concat(array2);  // Output: [1, 2, 3, 4]
console.log(combined);

// 7. join() - მასივის ელემენტების სტრიქონში გაერთიანება
console.log("\njoin() ფუნქცია:");
let fruits2 = ['apple', 'banana', 'cherry'];
let result = fruits2.join(', ');  // Output: 'apple, banana, cherry'
console.log(result);

// 8. slice() - მასივის ნაწილი
console.log("\nslice() ფუნქცია:");
let fruits3 = ['apple', 'banana', 'cherry', 'date'];
let sliced = fruits3.slice(1, 3);  // Output: ['banana', 'cherry']
console.log(sliced);

// 9. splice() - ელემენტების წაშლა ან ჩანაცვლება
console.log("\nsplice() ფუნქცია:");
let fruits4 = ['apple', 'banana', 'cherry'];
fruits4.splice(1, 1, 'orange');  // Output: ['apple', 'orange', 'cherry']
console.log(fruits4);

// 10. sort() - მასივის დალაგება
console.log("\nsort() ფუნქცია:");
let numbers4 = [4, 2, 5, 1];
numbers4.sort();  // Output: [1, 2, 4, 5]
console.log(numbers4);

// 11. indexOf() - ელემენტის ინდექსის მიღება
console.log("\nindexOf() ფუნქცია:");
let fruits5 = ['apple', 'banana', 'cherry'];
let index = fruits5.indexOf('banana');  // Output: 1
console.log(index);

// 12. push() - ელემენტის დამატება
console.log("\npush() ფუნქცია:");
let fruits6 = ['apple', 'banana'];
fruits6.push('cherry');  // Output: ['apple', 'banana', 'cherry']
console.log(fruits6);

// 13. pop() - ელემენტის წაშლა ბოლოს
console.log("\npop() ფუნქცია:");
let fruits7 = ['apple', 'banana', 'cherry'];
fruits7.pop();  // Output: ['apple', 'banana']
console.log(fruits7);

// 14. shift() - ელემენტის წაშლა პირველ ადგილზე
console.log("\nshift() ფუნქცია:");
let fruits8 = ['apple', 'banana', 'cherry'];
fruits8.shift();  // Output: ['banana', 'cherry']
console.log(fruits8);

// 15. unshift() - ელემენტის დამატება პირველ ადგილზე
console.log("\nunshift() ფუნქცია:");
let fruits9 = ['banana', 'cherry'];
fruits9.unshift('apple');  // Output: ['apple', 'banana', 'cherry']
console.log(fruits9);

// 16. find() - ელემენტის მოძებნა
console.log("\nfind() ფუნქცია:");
let numbers5 = [1, 2, 3, 4, 5];
let found = numbers5.find(function(number) {
    return number > 3;  // Output: 4
});
console.log(found);

// 17. every() - ყველა ელემენტის შემოწმება
console.log("\nevery() ფუნქცია:");
let numbers6 = [2, 4, 6, 8];
let allEven = numbers6.every(function(number) {
    return number % 2 === 0;  // Output: true
});
console.log(allEven);

// 18. some() - ნებისმიერ ელემენტზე შემოწმება
console.log("\nsome() ფუნქცია:");
let numbers7 = [1, 3, 5, 8];
let someEven = numbers7.some(function(number) {
    return number % 2 === 0;  // Output: true
});
console.log(someEven);

// 19. sort() - მასივის დალაგება (უმჯობესია ზუსტად მინიშნოთ თუ რა მნიშვნელობით უნდა დავალაგოთ)
console.log("\nsort() ფუნქცია:");
let numbers8 = [4, 2, 5, 1];
numbers8.sort(function(a, b) {
    return a - b;  // Output: [1, 2, 4, 5] - დალაგება ზრდის მიხედვით
});
console.log(numbers8);

// 20. reverse() - მასივის დაბრუნება უკუღმა
console.log("\nreverse() ფუნქცია:");
let fruits10 = ['apple', 'banana', 'cherry'];
fruits10.reverse();  // Output: ['cherry', 'banana', 'apple']
console.log(fruits10);

// 21. toString() - სტრიქონად გადაკეთება
console.log("\ntoString() ფუნქცია:");
let numbers9 = [1, 2, 3, 4];
let str = numbers9.toString();  // Output: '1,2,3,4'
console.log(str);

// 22. isArray() - მასივის შემოწმება
console.log("\nisArray() ფუნქცია:");
let isArray = Array.isArray([1, 2, 3]);  // Output: true
console.log(isArray);

// 23. slice() - მასივის ნაწილი (მაგალითით)
console.log("\nslice() ფუნქცია:");
let fruits11 = ['apple', 'banana', 'cherry', 'date'];
let part = fruits11.slice(1, 3);  // Output: ['banana', 'cherry']
console.log(part);





