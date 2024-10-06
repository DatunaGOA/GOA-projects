function modifyWord(word) {
    const midIndex = Math.ceil(word.length / 2); // Get the middle index
    const firstHalf = word.slice(0, midIndex); // Get the first half
    const secondHalf = word.slice(midIndex); // Get the second half
    return secondHalf + firstHalf; // Concatenate second half with first half
}
console.log(modifyWord("gamarjoba")); // Output: "rjobagamar"
