$(document).ready(function(){
    $(function(){
        $("#playlist li").on("click",function(){
            $("#videoarea").attr({
                src:$(this).attr("movieurl"),
            });
        });
        $("#videoarea").attr({
            src:$("#playlist li").eq(0).attr("movieurl"),
        });

    });


});
$(document).ready(function(){
    var $regexname=/^([a-zA-Z]{2,30})$/;
    $('.name').on('keypress keydown keyup',function(){
             if (!$(this).val().match($regexname)) {
              // there is a mismatch, hence show the error message
                 $('.emsg').removeClass('hidden');
                 $('.emsg').show();
             }
           else{
                // else, do not display message
                $('.emsg').addClass('hidden');
               }
         });
});