window.timer = 0;

const socket = io()

document.addEventListener('DOMContentLoaded', function(){

    console.log("Loaded Socket")
    // document.getElementById('ResetRobotLib').addEventListener('click', resetRobotLib)
    document.getElementById('listenerSocketActive').addEventListener("click", socketEnableCheck);
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