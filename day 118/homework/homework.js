class BankAccount {
    #balance = 0;
    getBalance() { return this.#balance; }
    deposit(amount) { this.#balance += amount; }
}

const account = new BankAccount();
account.deposit(100);
console.log(account.getBalance());
