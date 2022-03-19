window.timer = 0;

document.addEventListener('DOMContentLoaded', function(){

    console.log("Loaded")
    rcEnableCheck();
    document.getElementById('listenerActive').addEventListener("click", rcEnableCheck);
});



function rcEnableCheck() {

    console.log("Entered rcEnableCheck()")

    var isChecked = document.getElementById('listenerActive').checked;

    if(isChecked == true) {
        timer = setInterval(gpStatusSender, 50);
    }
    else {
        clearInterval(timer)
    }
}


function gpStatusSender() {

    console.log("Entered gpStatusSender()")

    gamepad = navigator.getGamepads()[0];

    var gpData = {
        axisX : gamepad.axes[0],
        axisY : gamepad.axes[1]
    }

    $.ajax({
        url: "/gamepad",
        data: JSON.stringify(gpData),
        type: 'POST',
        contentType: "application/json",
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}