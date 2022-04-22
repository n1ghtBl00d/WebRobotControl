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

function enableCheck() {
    console.log("entered socketEnableCheck")

    var isChecked = document.getElementById('listenerActive').checked;

    if(isChecked == true) {
        timer = setInterval(statusSender, 200);
    }
    else
    {
        clearInterval(timer)

        socket.emit("Stop", "Stop")
    }


}

function statusSender() {

    console.log("Entered statusSender()")

    gamepad = navigator.getGamepads()[0];

    
    var gpData = {
        axisLx : gamepad.axes[0],
        axisLy : gamepad.axes[1],
        axisRx : gamepad.axes[2],
        axisRy : gamepad.axes[3],
        btnUp : gamepad.buttons[0],
        btnDown : gamepad.buttons[1],
        btnLeft : gamepad.buttons[2],
        btnRight : gamepad.buttons[3],
        btnA : gamepad.buttons[4],
        btnB : gamepad.buttons[5],
        btnX : gamepad.buttons[6],
        btnY : gamepad.buttons[7],
        btnStart : gamepad.buttons[8],
        btnBack : gamepad.buttons[9],
        btnXbox : gamepad.buttons[10],
        btnLB : gamepad.buttons[11],
        btnRB : gamepad.buttons[12],
        btnLT : gamepad.buttons[13],
        btnRT : gamepad.buttons[14],
        btnLjoystick : gamepad.buttons[15],
        btnRjoystick : gamepad.buttons[16]
        
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