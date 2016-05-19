/**
 * Created by Dmitry Astrikov on 23.09.14.
 */
$(function(){
    $('form').each(function(index, element){
        $(element).validate();
    });
});