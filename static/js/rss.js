
$(document).ready(function(){
     

     $.ajax({
        url: '/rss_rus/',
        type: 'GET',
        dataType: "html",
        success: function(data) {
           $('#results_rss').html(data);
        }
    });  

})