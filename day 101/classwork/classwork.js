function checkTask() {
    return new Promise(resolve => setTimeout(() => resolve("shevamowmot davaleba"), 1000));
}

function completeTask() {
    return new Promise(resolve => setTimeout(() => resolve("davaleba shesrulds"), 2000));
}

function evaluateTask() {
    return new Promise((resolve, reject) => 
        setTimeout(() => Math.random() > 0.5 
            ? resolve("davaleba shesrulda magrad") 
            : reject("shegeshala"), 3000));
}

checkTask()
    .then(console.log)
    .then(completeTask)
    .then(console.log)
    .then(evaluateTask)
    .then(console.log)
    .catch(console.error);
