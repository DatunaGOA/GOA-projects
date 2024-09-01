// Select the form by its ID
const form = document.getElementById('userForm');

// Add an event listener to the form to listen for the submit event
form.addEventListener('submit', function(event) {
    // Prevent the form from submitting the traditional way
    event.preventDefault();

    // Get the values of the input fields
    const fullName = document.getElementById('fullName').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    // Check if any of the fields are empty
    if (fullName === "" || email === "" || password === "") {
        // If any field is empty, alert the user
        alert("All fields must be filled out");
    } else {
        // If all fields are filled, log the values to the console
        console.log("Full Name: " + fullName);
        console.log("Email: " + email);
        console.log("Password: " + password);

        // Optionally, you can now submit the form data to the server or perform other actions
        alert("All fields are filled out");
    }
});
