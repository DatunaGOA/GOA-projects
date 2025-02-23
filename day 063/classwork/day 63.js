// მასივის შექმნა 0-დან 100-ის ჩათვლით
let numbers = [];
for (let i = 0; i <= 100; i++) {
    numbers.push(i);
}

// ლუწი რიცხვების ჯამის გამოთვლა
let sumEven = 0;
for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
        sumEven += numbers[i];
    }
}

console.log("Sum of even numbers:", sumEven);



// მასივის შექმნა
let numbers1 = [10, 20, 30, 40, 50];

// ვცდილობთ გამოვიტანოთ ელემენტი 10 ინდექსზე (მასივში 5 ელემენტია, შესაბამისად ინდექსები 0-დან 4-მდეა)
console.log(numbers1[10]); //undefined




function manualSlice(array, startIndex, endIndex) {
    let result = [];
    
    // for ციკლი ინდექსების მიხედვით
    for (let i = startIndex; i < endIndex; i++) {
        result.push(array[i]);
    }
    
    return result;
}

// ფუნქციის გამოყენების მაგალითი
let numbers2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
let slicedArray = manualSlice(numbers, 2, 5);

console.log(slicedArray); // [30, 40, 50]
