/**
 * Created by orkan on 27.10.16.
 */
$(document).ready(function(){
    $('#cookie-info-container').on('click', function () {
        $.ajax('/agree-on-cookie-store');
        $(this).hide();
    });
});