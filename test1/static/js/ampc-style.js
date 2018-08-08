//(function ($, undefined) {
//
//    "use strict";
//
//    // When ready.
//    $(function () {
//        
//        var $form = $("#form");
////        var $input = $form.find( "input" );
//        var $input = $('#monthly-income');
//
//        $input.on("keyup", function (event) {
//            
//            
//            // When user select text in the document, also abort.
//            var selection = window.getSelection().toString();
//            if (selection !== '') {
//                return;
//            }
//            
//            // When the arrow keys are pressed, abort.
//            if ($.inArray(event.keyCode, [38, 40, 37, 39]) !== -1) {
//                return;
//            }
//            
//            
//            var $this = $(this);
//            
//            // Get the value.
//            var input = $this.val();
//            
//            var input = input.replace(/^([0-9]+(\.[0-9]+)?/gm, "");
//            input = input ? parseInt(input, 10) : 0;
//            $this.val(function () {
//                return (input === 0) ? "" : input.toLocaleString("en-US");
//            });
//        });
//        
//        /**
//         * ==================================
//         * When Form Submitted
//         * ==================================
//         */
//        $form.on("submit", function (event) {
//            
//            var $this = $(this);
//            var arr = $this.serializeArray();
//        
//            for (var i = 0; i < arr.length; i++) {
//                    arr[i].value = arr[i].value.replace(/^([0-9]+(\.[0-9]+)?/gm, ''); // Sanitize the values.
//            };
//            
//            console.log( arr );
//            
//            event.preventDefault();
//        });
//        
//    });
//})(jQuery);

//var text = document.getElementById('monthly-income');
//text.onkeypress = text.onpaste = checkInput;
//
//function checkInput(e) {
//    var e = e || event;
//    var char = e.type == 'keypress' 
//        ? String.fromCharCode(e.keyCode || e.which) 
//        : (e.clipboardData || window.clipboardData).getData('Text');
//    if (/[^\d.$]/gi.test(char)) {
//        return false;
//    }
//}
//
//
//function setTwoNumberDecimal(event) {
//    this.value = parseFloat(this.value).toFixed(2);
//}

$("#monthly-income").inputmask({"mask": "99 999.99"});
$("#weight").inputmask({"mask": "999.999"});

window.onload = setupRefresh();
        
function setupRefresh(){
    setInterval("refreshBlock();", 1000);
}
function refreshBlock(){
    var d = new Date();
    document.getElementById('timeS').innerHTML = d.toLocaleTimeString();
}