
const socket = io('https://chatbot-evertonlwf.cloud.okteto.net');

socket.on('connect', function () {
    console.log("Connected to Socket.io server");
});

let userName = 'Usuário';
let userslist = [];
let error = '';

let loginPage = document.querySelector('#loginPage');
let chatPage = document.querySelector('#chatPage');

let loginInput = document.querySelector('#loginNameInput');
let textInput = document.querySelector('#chatTextInput');

loginPage.style.display = 'none';
chatPage.style.display = 'flex';


socket.on('bot_uttered', function (response) {
    if (response.text) {
        console.log(response.text, "received text");
        addMessage('msg','Bot-1', response.text )
    }
    if (response.attachment) {
        console.log(response.attachment.payload.src, "received attachment");
        addMessage('msg','Bot-1', `<img src=${response.attachment.payload.src} alt="Minha Figura" height=200px></img>` )

    }
    if (response.quick_replies) {
        console.log(response.quick_replies, 'received quick_replies');
        addMessage('msg','Bot-1', response.quick_replies )

    }
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

//bot_uttered

loginInput.addEventListener('keyup',(e) => {
    if(e.keyCode === 13){
        let name = loginInput.value.trim();
        if(name !== ''){
            userName = name;
            document.title = `ChatBoot (${userName})`;
            socket.emit('session_request', {session_id: userName});
            loginPage.style.display = 'none';
            chatPage.style.display = 'flex';
            textInput.focus();
            addMessage('status',null,'Conectado');
        }
    }
})
/*
textInput.addEventListener('keyup', (e)=>{
    if(e.keyCode === 13){
        let txt = textInput.value.trim();
        textInput.value = '';
        if(txt !== ''){
            socket.emit('send-msg', txt);
        }
    }
})

socket.on('user-ok', (list)=>{
    loginPage.style.display = 'none';
    chatPage.style.display = 'flex';
    textInput.focus();
    addMessage('status',null,'Conectado');
    userList = list
    renderUserList();
});

socket.on('list-update', (data)=>{
    if(data.joined){
        addMessage('status',null, data.joined+' entrou no chat.' )
    }
    if(data.left){
        addMessage('status',null, data.left+' saiu do chat.' )
    }
    userList = data.list
    renderUserList();
});

socket.on('show-msg', (data)=>{
    if(data.message){
        addMessage('msg',data.username, data.message )
    }
});

socket.on('disconnect', ()=>{
    error = 'disconnect';
    addMessage('status',null, 'você foi desconectado!' );
});

socket.on('connect_error', ()=>{
    addMessage('status',null, 'tentando reconectar...' );
});

socket.on('connect', ()=>{
    if(error != ''){
        addMessage('status',null, 'Reconectado!' );
        if (userName != '') {
            socket.emit('join-request', userName);
        }
    }
});



*/

function renderUserList() {
    let ul = document.querySelector('.userList');
    ul.innerHTML = '';

    userList.forEach(e => {
        ul.innerHTML += '<li>'+e+'</li>';
    });
}

function addMessage(type, user, msg) {
    let ul = document.querySelector('.chatList');
    switch (type) {
        case 'status':
            ul.innerHTML += '<li class="m-status"> '+msg+'</li>'
            break;
    
        case 'msg':
            ul.innerHTML += `<li class="m-txt"><span class=${userName==user? "me" : ""} >${user}</span> ${msg}</li>`
            break;
    }
    ul.scrollTop = ul.scrollHeight;
} 