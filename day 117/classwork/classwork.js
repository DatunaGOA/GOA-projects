const jokes = [
    { setup: "რატომ უყვართ ებრაელებს ბანაობა?", punchline: "იმიტორო ისტორია აქვთ საპონთან" },
    { setup: "ჩემი ძმაკაცი როცა მოკვდა მასთან ახლო არ ვიყავი", punchline: "კიდევ კარგი იმიტორო ბომბი აუფეთქდა" },
    { setup: "რა აქვთ მამაჩემს და ნემოს საერთო?", punchline: "ორივეს დღემდე ეძებენ" },
    { setup: "ბევრი ხუმრობა მაქვს ხალხზე რომლებსაც სამსახური არ აქვთ", punchline: "მაგრამ არცერთი მუშაობს" },
];

function showJoke() {
    let joke = jokes[Math.floor(Math.random() * jokes.length)];
    document.getElementById("setup").textContent = joke.setup;
    let punchline = document.getElementById("punchline");
    punchline.textContent = joke.punchline;
}
//i used w3schools to help me btw