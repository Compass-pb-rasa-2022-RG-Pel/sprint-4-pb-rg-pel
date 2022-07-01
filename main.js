const socket = io('http://localhost:5005/');
//const socket = io();

socket.on('connect', function () {
    console.log("Connected to Socket.io server");
});