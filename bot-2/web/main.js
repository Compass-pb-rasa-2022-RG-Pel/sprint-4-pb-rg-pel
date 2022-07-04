const socket = io('http://localhost:5005');
//const socket = io();

socket.on('connect', function () {
    console.log("Connected to Socket.io server");
    socket.emit('session_request', {session_id: "algo aqui dentro"});

});

let textInput = document.querySelector('#chatTextInput');


socket.on('bot_uttered', function (response) {
    console.log(response)
});

textInput.addEventListener('keyup', (e)=>{
    if(e.keyCode === 13){
        let txt = textInput.value.trim();
        textInput.value = '';
        if(txt !== ''){
            socket.emit('user_uttered', {
                "message": txt,
            });
            addMessage('msg',userName, txt )
        }
    }
})