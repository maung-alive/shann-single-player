const cards = ['10_of_clubs.png', '10_of_diamonds.png', '10_of_hearts.png', '10_of_spades.png', '2_of_clubs.png', '2_of_diamonds.png', '2_of_hearts.png', '2_of_spades.png', '3_of_clubs.png', '3_of_diamonds.png', '3_of_hearts.png', '3_of_spades.png', '4_of_clubs.png', '4_of_diamonds.png', '4_of_hearts.png', '4_of_spades.png', '5_of_clubs.png', '5_of_diamonds.png', '5_of_hearts.png', '5_of_spades.png', '6_of_clubs.png', '6_of_diamonds.png', '6_of_hearts.png', '6_of_spades.png', '7_of_clubs.png', '7_of_diamonds.png', '7_of_hearts.png', '7_of_spades.png', '8_of_clubs.png', '8_of_diamonds.png', '8_of_hearts.png', '8_of_spades.png', '9_of_clubs.png', '9_of_diamonds.png', '9_of_hearts.png', '9_of_spades.png', 'ace_of_clubs.png', 'ace_of_diamonds.png', 'ace_of_hearts.png', 'ace_of_spades.png', 'jack_of_clubs.png', 'jack_of_diamonds.png', 'jack_of_hearts.png', 'jack_of_spades.png', 'king_of_clubs.png', 'king_of_diamonds.png', 'king_of_hearts.png', 'king_of_spades.png', 'queen_of_clubs.png', 'queen_of_diamonds.png', 'queen_of_hearts.png', 'queen_of_spades.png']
const playButton = document.querySelector(".play-btn");

if(playButton){
    playButton.addEventListener('click', () => {
        let text = document.querySelector('.welcome');
        document.querySelector('.fire-gif').style.display = "block";
        document.querySelector('.progress').style.display = "block";
        text.className += " wrinkles"
        playButton.innerHTML = "စောင့်ပါ"
        playButton.style.backgroundColor = "inherit";
        let progress = document.querySelector(".progress-value");
        const images = [];
        var dotCount = 0;
        for (let i = 0; i < cards.length; i++) {
            let temp = new Image()
            images.push(temp)
            temp.src = `static/images/cards/${cards[i]}`
            temp.addEventListener('load', () => {
                playButton.innerHTML = `စောင့်ပါ${".".repeat(dotCount)}`
                dotCount > 3 ? dotCount=0 : dotCount++
                document.querySelector('.progress-percent').innerHTML = `${Math.floor((i/cards.length) * 100)}%`
                progress.style.width = `${Math.floor((i/cards.length) * 100)}%`
            })
        }
        document.location.href = "/play"
    })
}

const usernameInput = document.querySelector('input[type="text"]')
if(usernameInput){
    usernameInput.addEventListener('focus', () => {
        document.querySelector('.form').classList.add('active')
    })
}

const form = document.querySelector('.form')
if(form){
    form.addEventListener('submit', (e) => {
        if(usernameInput.value.length < 3){
            e.preventDefault()
            document.querySelector('.form-error').innerHTML = "အသုံးမပြုနိုင်ပါသေးပါ"
        }
    })
}

const gameStart = document.querySelector("#game-start")
const gameStop = document.querySelector("#game-stop")
if(gameStart){
    gameStart.addEventListener('click', () => {
        fetch('/play/game/take', {})
        .then(res => res.json())
        .then(res => {
            document.querySelector(`#${res.username}`).innerHTML += `<img src="/static/images/cards/${res.card.img}" alt="card-back" class="card back" style="left:80px;">`
        })
    })

    gameStop.addEventListener('click', () => {
        fetch('/play/game/winners', {})
       .then(res => res.json())
       .then(res => {
            res.players.forEach(winner => {
                let parentDiv = document.querySelector(`#${winner.name.split(" ").join("")}`)
                parentDiv.style.opacity = 0.5
                parentDiv.innerHTML = ""
                winner.cards.forEach(card => {
                    parentDiv.innerHTML += `<img src="/static/images/cards/${card.img}" alt="card" class="card back">`
                })
                parentDiv.innerHTML += `<span class="username">${winner.name}</span>`
            })
            res.winners.forEach(winner => {
                let parentDiv = document.querySelector(`#${winner.name.split(" ").join("")}`)
                parentDiv.style.opacity = 1
                parentDiv.setAttribute("style", `${parentDiv.getAttribute('style')}-webkit-filter: drop-shadow(5px 5px 5px #222);`);
            })
            gameStop.innerHTML = "ပြန်စမယ်"
            gameStop.onclick = () => document.location.href = '/'
       })
    })
}