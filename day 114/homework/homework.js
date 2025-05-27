class Student {
    constructor(score) { this.score = score; }
    get grade() {
        return this.score >= 90 ? "A" :
               this.score >= 80 ? "B" :
               this.score >= 70 ? "C" :
               this.score >= 60 ? "D" : "F";
    }
}


const student = new Student(85);
console.log(student.grade);
