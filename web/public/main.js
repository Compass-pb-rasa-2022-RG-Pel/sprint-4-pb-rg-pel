// const socket = io('http://localhost:5005')

const socket = io()
socket.on('connect', function () {
    console.log("conectou")
    
})

let textInput = document.querySelector('#msg')
textInput.addEventListener('keyup', (e) => {
    if(e.keyCode === 13) {
        let txt = textInput.value.trim()
        textInput.value = ''
        if(txt !== ''){
            socket.emit('user_uttered', {'message':txt})
        }
    }
})

socket.on('bot_uttered', function (resp) {
    console.log(resp)

    

    teste(response.text)
})

function teste(msg) {
    let ul = document.querySelector('.cat')
    ul.innerHTML += '<li>'+msg+'</li>'
}

