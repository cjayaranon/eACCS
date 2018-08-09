//Capitalize first letter while typing in side of input field
jQuery(document).ready(function($) {
    $('.cap-field').keyup(function(event) {
        var textBox = event.target;
        var start = textBox.selectionStart;
        var end = textBox.selectionEnd;
        textBox.value = textBox.value.charAt(0).toUpperCase() + textBox.value.slice(1);
        textBox.setSelectionRange(start, end);
    });
});

//credits https://gist.github.com/alex-gist/2025270