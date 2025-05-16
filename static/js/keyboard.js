function loop() {
    requestAnimationFrame(loop);
}

loop();

window.timer = 0;

const socket = io()
var imageFeed = -1
var imgData = -1

var wValue = false
var aValue = false
var sValue = false
var dValue = false
var qValue = false
var eValue = false
var shiftValue = false

kd.W.down(function () {
    wValue = true
});
kd.W.up(function () {
    wValue = false
});

kd.A.down(function () {
    aValue = true
});
kd.A.up(function () {
    aValue = false
});

kd.S.down(function () {
    sValue = true
});
kd.S.up(function () {
    sValue = false
});

kd.D.down(function () {
    dValue = true
});
kd.D.up(function () {
    dValue = false
});

kd.Q.down(function () {
    qValue = true
});
kd.Q.up(function () {
    qValue = false
});

kd.E.down(function () {
    eValue = true
});
kd.E.up(function () {
    eValue = false
});

kd.SHIFT.down(function () {
    shiftValue = true
});
kd.SHIFT.up(function () {
    shiftValue = false
});

document.addEventListener('DOMContentLoaded', function () {
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

    if (isChecked == true) {
        timer = setInterval(statusSender, 200);
    }
    else {
        clearInterval(timer)

        socket.emit("Stop", "Stop")
    }


}

function statusSender() {

    console.log("Entered statusSender()")

    kd.tick();

    var xValue = 0
    var yValue = 0
    var rValue = 0
    var mValue = 1


    if (wValue) {
        yValue += 1
    }
    if (sValue) {
        yValue -= 1
    }

    if (aValue) {
        xValue += 1
    }
    if (dValue) {
        xValue -= 1
    }

    if (qValue) {
        rValue += 1
    }
    if (eValue) {
        rValue -= 1
    }

    if (shiftValue) {
        mValue /= 2
    }

    xValue *= mValue
    yValue *= mValue
    rValue *= mValue

    var gpData = {
        axisLx: xValue,
        axisLy: yValue,
        axisRx: rValue,
        axisRy: 0
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
    if (data.imgString != null) {
        imageFeed.src = data.imgString
    }

})