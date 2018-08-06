var text = document.getElementById('monthly-income');
text.onkeypress = text.onpaste = checkInput;

var regex = /^[1-9]$/;

function checkInput(e) {
    var e = e || event;
    var char = e.type == 'keypress' ?  String.fromCharCode(e.keyCode || e.which) 
        : (e.clipboardData || window.clipboardData).getData('Text');
    if (/^([0-9]+(\.[0-9]+)?)/gi.test(char)) {
        return false;
    }
}