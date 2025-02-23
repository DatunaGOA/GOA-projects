// 1
const task1 = new Promise((resolve) => {
    setTimeout(() => resolve("Task 1 complete"), 2000);
});
task1.then(console.log);

// 2
const task2 = new Promise((_, reject) => {
    reject("Task 2 failed");
});
task2.catch(console.error);

// 3
const task3 = new Promise((resolve) => resolve(5))
    .then((num) => num * 2)
    .then(console.log);

// 4
const task4 = () =>
    new Promise((resolve) => {
        setTimeout(() => resolve("First"), 2000);
    });
task4().then((msg) =>
    setTimeout(() => console.log("Second"), 1000)
);

// 5
const task5 = () =>
    new Promise((_, reject) =>
        setTimeout(() => reject("Task 3 failed"), 2000)
    );
task5().catch(console.error);

// 6
const task6 = () =>
    new Promise((resolve) => {
        const delay = Math.random() * 4000 + 1000;
        setTimeout(() => resolve("Task 1 complete"), delay);
    });
task6().then(console.log);

// 7
const task7 = () =>
    new Promise((resolve) => {
        const delay1 = Math.random() * 2000 + 1000;
        setTimeout(() => resolve("First"), delay1);
    }).then((msg) => {
        const delay2 = Math.random() * 2000 + 1000;
        setTimeout(() => console.log("Second"), delay2);
    });
task7();

// 8
const task8 = () =>
    new Promise((_, reject) => {
        const delay = Math.random() * 3000 + 1000;
        setTimeout(() => reject("Task 3 failed"), delay);
    });
task8().catch(console.error);

// 9
const task9 = () =>
    new Promise((resolve) => {
        const delay = Math.random() * 4000 + 1000;
        const random = Math.random();
        setTimeout(
            () =>
                resolve(
                    random > 0.5 ? "Task 1 complete" : "Task 1 was quick"
                ),
            delay
        );
    });
task9().then(console.log);

// 10
const task10 = () =>
    new Promise((resolve, reject) => {
        const delay = Math.random() * 3000 + 1000;
        const random = Math.random();
        setTimeout(() => {
            if (random < 0.3) reject("Task 3 failed");
            else resolve("Task 3 complete");
        }, delay);
    });
task10().then(console.log).catch(console.error);
