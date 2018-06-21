
        jQuery(function(){

$(document).ready(function(){
    $("#name").blur(function(){

        alert("ss");
        var contents = $("#name").val();
            $("#t1").val(contents);
    });
});
});
