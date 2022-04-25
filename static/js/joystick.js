

let joystick1 = new JoystickController("stick1", 64, 8);
let joystick2 = new JoystickController("stick2", 64, 8);

function loop()
{
	requestAnimationFrame(loop);
}

loop();

window.timer = 0;

const socket = io()
var imageFeed = -1
var imgData = -1

document.addEventListener('DOMContentLoaded', function(){

    console.log("Loaded Socket")
    imageFeed = document.getElementById('camFeed')
    // document.getElementById('ResetRobotLib').addEventListener('click', resetRobotLib)
    document.getElementById('listenerActive').addEventListener("click", enableCheck);
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

    
    var gpData = {
        axisLx : joystick1.value["x"],
        axisLy : joystick1.value["y"],
        axisRx : joystick2.value["x"],
        axisRy : joystick2.value["y"]

        
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