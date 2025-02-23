function findLongest(array){
    let mostDigitNumber = array[0]
    let mostDigit = 0
    
    for(let i = 0; i < array.length; i++){
      const currentNumber = array[i];
      const numberOfDigits = currentNumber.toString().length;
      
      if(mostDigit < numberOfDigits){
        mostDigit = numberOfDigits
        mostDigitNumber = currentNumber
      }
    }
    
    return mostDigitNumber
  }