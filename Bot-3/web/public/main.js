const socket = io("http://localhost:5005")
socket.on("connect", function () {
    console.log("conectado")
    socket.emit("session_request", { session_id: "Rodrigo" })
})

socket.on("bot_uttered", function (response) {
    console.log(response)
    posta1(response.text)

})

function gif1() {
    let quandoDigitar = document.getElementById("mensagem1").value
    if (quandoDigitar == "" || quandoDigitar.length >= 1)
        document.getElementById('demo1').style.display = 'block'
    quandoDigitar = document.getElementById("mensagem1").value
    if (quandoDigitar == "" || quandoDigitar.length == 0)
        document.getElementById('demo1').style.display = 'none'
}

function posta1(txt) {
    const a = document.createElement("div")
    let texto = ''
    if (txt == undefined) {
        texto = document.getElementById("mensagem1").value
        if (texto !== "") {
            socket.emit("user_uttered", { "message": texto })
        }
        a.setAttribute("class", "msg_cotainer")
        a.setAttribute("id", "chateu")
        a.innerHTML = '  Cliente' + "<br>" + texto + "<br>" + RetornaHoraAtual(image1())

    } else {
        texto = txt
        if (texto.match("https://") || texto.match("http://")) {
            texto = `<a href=${texto} target="_blank">${texto}<a/>`
        };
        a.setAttribute("class", "msg_cotainer")
        a.setAttribute("id", "chateu")
        a.innerHTML = '<p>Bot  ' + "<br>" + texto + "<br><p/>" + RetornaHoraAtual(image2())
    }


    document.getElementById("chatoutro").appendChild(a)
    document.getElementById("mensagem1").value = ""
    document.getElementById("mensagem1").focus()
    const quandoDigitar = document.getElementById("mensagem1").value
    if (quandoDigitar == "" || quandoDigitar.length == 0)
        document.getElementById('demo1').style.display = 'none'
}
function image1() {
    const img1 = document.createElement("img")
    img1.setAttribute("class", "rounded-circle user_img_msg_2")
    img1.src = "https://i.ibb.co/TTHsRgr/user1.jpg"
    document.getElementById("chatoutro").appendChild(img1)
}

function image2() {
    const img1 = document.createElement("img")
    img1.setAttribute("class", "rounded-circle user_img_msg_1")
    img1.src = "https://i.ibb.co/C5WfM7R/user2.jpg"
    document.getElementById("chatoutro").appendChild(img1)
}
function RetornaHoraAtual() {
    const dNow = new Date()
    const minutos = String(dNow.getMinutes()).padStart(2, "0")
    const localdate = dNow.getHours() + ':' + minutos
    return localdate;
}
