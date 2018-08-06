var text = document.getElementById('monthly-income');
text.onkeypress = text.onpaste = checkInput;

function checkInput(e) {
    var e = e || event;
    var char = e.type == 'keypress' 
        ? String.fromCharCode(e.keyCode || e.which) 
        : (e.clipboardData || window.clipboardData).getData('Text');
    if (/[^(?!0\.00)[1-9]\d{0,2}(,\d{3})*(\.\d\d)?$]/gi.test(char)) {
        return false;
    }
}