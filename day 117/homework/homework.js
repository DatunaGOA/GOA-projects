class MathHelper {
    static PI = 3.14159;
    static power(base, exp) { return base ** exp; }
}

class RandomHelper {
    static CHAR_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    static randomChar() { return this.CHAR_SET[Math.floor(Math.random() * this.CHAR_SET.length)]; }
}
