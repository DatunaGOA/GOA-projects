window.onload = function() {
    const greetingElement = document.querySelector('#hero h1');
    const currentTime = new Date().getHours();

    if (currentTime < 12) {
        greetingElement.innerText = 'Good Morning! Welcome to Our Website';
    } else if (currentTime < 18) {
        greetingElement.innerText = 'Good Afternoon! Welcome to Our Website';
    } else {
        greetingElement.innerText = 'Good Evening! Welcome to Our Website';
    }
};
