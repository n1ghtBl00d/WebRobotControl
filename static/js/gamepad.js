window.timer = 0;

document.addEventListener('DOMContentLoaded', function(){

    console.log("Loaded")
    // document.getElementById('ResetRobotLib').addEventListener('click', resetRobotLib)
    document.getElementById('listenerActive').addEventListener("click", rcEnableCheck);
});



function rcEnableCheck() {

    console.log("Entered rcEnableCheck()")

    var isChecked = document.getElementById('listenerActive').checked;

    if(isChecked == true) {
        timer = setInterval(gpStatusSender, 200);
    }
    else {
        clearInterval(timer)
        $.ajax({
            url: "/stop",
            data: "STOP!!!!!!!!!!",
            type:'POST',
            contentType: "application/text",
            success: function(response) {
                console.log(response);
                console.log("Stopped")
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
}


function gpStatusSender() {

    console.log("Entered gpStatusSender()")

    gamepad = navigator.getGamepads()[0];

    ////This is the Data object for Arcade Drive and Self-Balancing input
    // var gpData = {
    //     axisX : gamepad.axes[0],
    //     axisY : gamepad.axes[1],
    //     buttonUp : gamepad.buttons[12].value,
    //     buttonDown : gamepad.buttons[13].value
    // }

    //This is the Data object for Tank Drive
    var gpData = {
        axisL : gamepad.axes[1],
        axisR : gamepad.axes[0]
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

//Not yet used
function ResetRobotLib(){
    activeLib = document.getElementById('RobotLib').innerText

    $.ajax({
        url: "/reset",
        data: activeLib,
        type: "POST",
        contentType: "text",
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    })

}