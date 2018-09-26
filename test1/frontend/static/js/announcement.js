(function() {
    $("#search-submit").click(function() {
        var request = $.ajax({
            type: "get",
            url: "/books/search/",
            data: {'q': $("#search-query").val()},
            beforeSend: function() {
                
            },
            
            success: function(response) {
                var json_response = JSON.parse(response);
                $('#search-results').empty()
                for (var i=0; i<json_response.length; i++) {
                    $('#search-results').append("<li>"+json_response[i].fields['title']+"</li>")
                }
            },
            
            error: function(response) {
                console.log(response.responseText);
                $('#search-results').empty()
                $('#search-results').append("<li style=color:red>"+response.responseText.slice(1,-1)+"</li>")
            }
        });
    });
})();