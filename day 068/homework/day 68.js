
function handleClick(event) {
    alert(`You clicked on ${event.currentTarget.id}`);
}

// Adding event listeners for bubbling phase
document.getElementById('div1').addEventListener('click', handleClick);
document.getElementById('div2').addEventListener('click', handleClick);
document.getElementById('div3').addEventListener('click', handleClick);

// For capturing phase, we need to set the third parameter to true
document.getElementById('div1').addEventListener('click', handleClick, true);
document.getElementById('div2').addEventListener('click', handleClick, true);
document.getElementById('div3').addEventListener('click', handleClick, true);
