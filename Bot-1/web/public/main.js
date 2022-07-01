const socket = io("http://localhost:5005")
socket.on("connect",function () {
    console.log("conectado")
    socket.emit("session_request", {session_id:"tatieli"})
})
let textinput=document.querySelector("#input")
textinput.addEventListener("keyup",(e)=>{
    if(e.keyCode===13){
        let txt=textinput.value.trim()
        textinput.value=""
        if(txt!==""){
            socket.emit("user_uttered", {"message":txt}) 
            doguinhos("(usuario) " + txt)
        }
    }
})
socket.on("bot_uttered", function (response) {
    console.log(response)


    doguinhos("(bot) " + response.text)

})

function doguinhos(msg) {
    let ul = document.querySelector(".dogs")
    ul.innerHTML += '<li>'+msg+'</li>'
}