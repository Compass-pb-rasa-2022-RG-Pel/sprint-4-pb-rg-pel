const socket = io("http://localhost:5005")
socket.on("connect",function () {
    console.log("conectado")
    socket.emit("session_request", {session_id:"suelen"})
})
let textinput=document.querySelector("#input")
textinput.addEventListener("keyup",(e)=>{
    if(e.keyCode===13){
        let txt=textinput.value.trim()
        textinput.value=""
        if(txt!==""){
            socket.emit("user_uttered", {"message":txt}) 
            insert_cats("(user) " + txt)
        }
    }
})
socket.on("bot_uttered", function (resp) {
    console.log(resp)


    insert_cats("(bot) " + resp.text)

})

function insert_cats(msg) {
    let ul = document.querySelector(".chat")
    ul.innerHTML += '<li>'+msg+'</li>'
}

