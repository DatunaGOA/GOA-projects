let person = {
    firstName: 'SHota',
    lastName: 'Rustaveli'
  };
  
  person.name = person.firstName + ' ' + person.lastName;
  
  delete person.firstName;
  delete person.lastName;

  person.emailList = ["shotarustaveli69.gmail.com"];
  person.passwordList = ["**********"];

  console.log(person);
  