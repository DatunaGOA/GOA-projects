class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    get initials() {
        return `${this.firstName[0]}${this.lastName[0]}`;
    }
}


const person = new Person("data", "barbakadze");
console.log(person.initials);
