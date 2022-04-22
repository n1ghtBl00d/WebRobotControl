window.timer = 0;

const socket = io()
var imageFeed = -1
var imgData = -1

document.addEventListener('DOMContentLoaded', function(){

    console.log("Loaded Socket")
    imageFeed = document.getElementById('camFeed')
    // document.getElementById('ResetRobotLib').addEventListener('click', resetRobotLib)
    document.getElementById('listenerActive').addEventListener("click", socketEnableCheck);
    document.getElementById('startCam').addEventListener("click", startCam);
    document.getElementById('stopCam').addEventListener("click", stopCam);
});

function socketEnableCheck() {
    console.log("entered socketEnableCheck")

    var isChecked = document.getElementById('listenerSocketActive').checked;

    if(isChecked == true) {
        timer = setInterval(socketStatusSender, 200);
    }
    else
    {
        clearInterval(timer)

        socket.emit("Stop", "Stop")
    }


}

function socketStatusSender() {

    console.log("Entered gpStatusSender()")

    gamepad = navigator.getGamepads()[0];

    
    var gpData = {
        axisL : gamepad.axes[1],
        axisR : gamepad.axes[0]
    }

    socket.emit("robotControl", gpData)

}

function startCam() {
    console.log("StartCam()")
    socket.emit("startCamera", "Start")
}
function stopCam() {
    console.log("stopCam()")
    socket.emit("stopCamera", "Stop")
}

socket.on("camera", (data) => {
    imgData = data
    console.log("Image Data: " + data.imgString)
    if (data.imgString != null)
    {
        imageFeed.src = data.imgString
    }
    
})